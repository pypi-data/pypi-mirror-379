# Copyright (c) 2022, California Institute of Technology and contributors
#
# You should have received a copy of the licensing terms for this
# software included in the file "LICENSE" located in the top-level
# directory of this package. If you did not, you can view a copy at
# https://git.ligo.org/ngdd/arrakis-server/-/raw/main/LICENSE

from __future__ import annotations

import argparse
import logging
import sys
import threading
from collections import defaultdict
from collections.abc import Generator, Iterable, Iterator
from datetime import timedelta
from pathlib import Path

import appdirs
import gpstime
import pyarrow
import pyarrow.compute
from arrakis import Time
from arrakis.block import SeriesBlock, combine_blocks
from arrakis.mux import Muxer
from arrakis_server.channel import Channel
from arrakis_server.metadata import ChannelConfigBackend
from arrakis_server.scope import Retention, ScopeInfo
from arrakis_server.traits import PublishServerBackend
from confluent_kafka import Consumer, TopicPartition

logger = logging.getLogger("arrakis")

DEFAULT_TIMEOUT = timedelta(seconds=1)


class KafkaBackend(PublishServerBackend):
    """Backend serving timeseries data from Kafka."""

    def __init__(self, kafka_url: str, publisher_configs: list[Path] | None):
        self.kafka_url = kafka_url
        logger.info("kafka URL: %s", self.kafka_url)

        # cache file for self-updating publishers
        # FIXME: how better to manage who can do this
        cache_dir = Path(appdirs.user_cache_dir("arrakis", "server"))
        cache_dir.mkdir(exist_ok=True)
        cache_file = cache_dir / "metadata.toml"
        logger.info("channel cache file: %s", cache_file)

        # load publisher channels
        self.metadata = ChannelConfigBackend(
            cache_file=cache_file,
            enforce=["publisher", "partition_id"],
        )
        if publisher_configs:
            for pconf in publisher_configs:
                publisher_id = pconf.stem
                logger.info("loading publisher '%s': %s", publisher_id, pconf)
                added = self.metadata.load(
                    pconf,
                    publisher=publisher_id,
                    overwrite=False,
                )
                if logger.getEffectiveLevel() <= logging.DEBUG:
                    for channel in added:
                        logger.debug(
                            "  %s partition_id=%s",
                            channel.name,
                            channel.partition_id,
                        )

        self._channels = set(self.metadata.metadata.values())

        self.scope_info = ScopeInfo(self.metadata.scopes, Retention.from_live_only())

        # lock used for updating partition table
        self._lock = threading.Lock()

    @staticmethod
    def add_arguments(parser):
        parser.add_argument(
            "--kafka-url",
            type=str,
            metavar="URL",
            required=True,
            help="URL pointing to a running kafka pool",
        )
        parser.add_argument(
            "--publisher-config",
            dest="publisher_configs",
            type=Path,
            metavar="PATH",
            action="append",
            help="path to publisher config TOML file or directory",
        )

    @classmethod
    def from_args(cls, args: argparse.Namespace) -> KafkaBackend:
        return cls(
            kafka_url=args.kafka_url,
            publisher_configs=args.publisher_configs,
        )

    def find(
        self,
        *,
        pattern: str,
        data_type: list[str],
        min_rate: int,
        max_rate: int,
        publisher: list[str],
    ) -> Iterable[Channel]:
        """Retrieve metadata for the 'find' route."""
        assert isinstance(self.metadata, ChannelConfigBackend)
        return self.metadata.find(
            pattern=pattern,
            data_type=data_type,
            min_rate=min_rate,
            max_rate=max_rate,
            publisher=publisher,
        )

    def describe(self, *, channels: Iterable[str]) -> Iterable[Channel]:
        """Retrieve metadata for the 'find' route."""
        assert isinstance(self.metadata, ChannelConfigBackend)
        return self.metadata.describe(channels=channels)

    def stream(
        self, *, channels: Iterable[str], start: int, end: int
    ) -> Iterator[SeriesBlock]:
        """Retrieve timeseries data for the 'stream' route."""
        assert isinstance(self.metadata, ChannelConfigBackend)
        # Query for channel metadata
        metadata = [self.metadata.metadata[channel] for channel in channels]

        is_live = not start and not end
        if is_live:
            yield from self._generate_live_series(metadata)
        else:
            raise NotImplementedError

    def _generate_live_series(
        self, channels: Iterable[Channel]
    ) -> Iterator[SeriesBlock]:
        assert isinstance(self.metadata, ChannelConfigBackend)
        dt = int((1 / 16) * Time.SECONDS)
        start = (int(gpstime.gpsnow() * Time.SECONDS) // dt) * dt

        # generate live data continuously
        partitions = {
            name: channel.partition_id
            for name, channel in self.metadata.metadata.items()
            if channel.partition_id
        }
        with Connection(self.kafka_url, partitions, channels) as conn:
            for block in conn.read(start=start):
                yield block

    def publish(self, *, publisher_id: str) -> dict[str, str]:
        """Retrieve connection info for the 'publish' route."""
        # FIXME: incorporate the producer ID with auth verification
        return {"bootstrap.servers": self.kafka_url}

    def partition(
        self, *, publisher_id: str, channels: Iterable[Channel]
    ) -> Iterable[Channel]:
        assert isinstance(self.metadata, ChannelConfigBackend)

        # assign any new partitions
        changed = set(channels) - self._channels
        if changed:
            for channel in changed:
                assert channel.publisher == publisher_id
            with self._lock:
                self.metadata.update(
                    list(changed),
                    overwrite=True,
                )
                self.channels = {channel for channel in self.metadata.metadata.values()}
                # always limit our response to the input list.
                # always send something so that the partition field is set
                channels = [
                    self.metadata.metadata[channel.name] for channel in channels
                ]

        return channels


class Connection:
    """A connection object to read data from Kafka."""

    def __init__(
        self, server: str, partitions: dict[str, str], channels: Iterable[Channel]
    ):
        """Create a Kafka connection.

        Parameters
        ----------
        server : str
            The Kafka broker to connect to.
        channels : Iterable[Channel]
            The channels requested.

        """
        self._channels = list(channels)
        self._channel_map = {channel.name: channel for channel in channels}
        self._partitions = partitions

        # group channels by partitions
        self._partition_map = defaultdict(list)
        for channel in channels:
            if channel.name in partitions:
                partition = partitions[channel.name]
                self._partition_map[partition].append(channel.name)

        # create Kafka consumer
        consumer_settings = {
            "bootstrap.servers": server,
            "group.id": "some.groupid",
            "message.max.bytes": 10_000_000,  # 10 MB
            "enable.auto.commit": False,
            "auto.offset.reset": "LATEST",
        }
        self._consumer = Consumer(consumer_settings)
        self._topics = [
            f"arrakis-{partition}" for partition in self._partition_map.keys()
        ]

    def read(
        self,
        start: int | None = None,
        poll_timeout: timedelta = DEFAULT_TIMEOUT,
    ) -> Generator[SeriesBlock, None, None]:
        """Read buffers from Kafka. Requires an open connection.

        Parameters
        ----------
        start : numeric, optional
            The GPS time to start receiving buffers for.
            Defaults to 'now'.
        max_latency : timedelta, optional
            The maximum latency to wait for messages.
            Default is 1 second.
        poll_timeout : timedelta, optional
            The maximum time to wait for a single message from Kafka.
            Default is 1 second.

        Yields
        ------
        buffers : dict of Buffers, keyed by str
            buffers, keyed by channel name

        """
        # if start time is specified, adjust the consumer's
        # offset to point at the data requested
        if start:
            # convert to UNIX time in ms
            offset_time = int(gpstime.gps2unix(start // Time.SECONDS) * 1000)
            # get offsets corresponding to times
            partitions = [
                TopicPartition(topic, partition=0, offset=offset_time)
                for topic in self._topics
            ]
            partitions = self._consumer.offsets_for_times(partitions)
            # reassign topic partitions to consumer
            self._consumer.unsubscribe()
            self._consumer.assign(partitions)
        else:
            offset_time = 0

        # set up muxer to multiplex buffers
        self._muxer: Muxer[pyarrow.RecordBatch] = Muxer(
            self._partition_map.keys(), start=start
        )

        # consume buffers from Kafka
        try:
            while True:
                msg = self._consumer.poll(timeout=poll_timeout.total_seconds())
                if msg and not msg.error():
                    # deserialize message then add to muxer
                    # and pull time-ordered buffers from it
                    partition = msg.topic().split("-", 1)[1]
                    with pyarrow.ipc.open_stream(msg.value()) as reader:
                        for batch in read_all_batches(reader):
                            # downselect channels
                            time = batch.column("time").to_numpy()[0]
                            batch = batch.filter(
                                pyarrow.compute.is_in(
                                    pyarrow.compute.field("channel"),
                                    pyarrow.array(self._partition_map[partition]),
                                ),
                            )
                            self._muxer.push(time, partition, batch)

                            # pull muxed blocks and combine
                            for muxed_batch in self._muxer.pull():
                                yield combine_blocks(
                                    *[
                                        SeriesBlock.from_row_batch(
                                            batch, self._channel_map
                                        )
                                        for batch in muxed_batch.values()
                                    ]
                                )

        except Exception as e:
            print(e, file=sys.stderr)

    def __iter__(self) -> Generator[pyarrow.RecordBatch, None, None]:
        """Read buffers from Kafka. Requires an open connection.

        Calls read() with default parameters.

        """
        yield from self.read()

    def open(self) -> None:
        """Open a connection to Kafka, subscribing to all required topics."""
        logger.debug("creating kafka subscription to topics: %s", self._topics)
        self._consumer.subscribe(self._topics)

    def close(self) -> None:
        """Closes a connection to Kafka, unsubscribing from all topics."""
        self._consumer.unassign()
        self._consumer.unsubscribe()
        self._consumer.close()

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, *args):
        self.close()


def read_all_batches(
    reader: pyarrow.ipc.RecordBatchStreamReader,
) -> Iterator[pyarrow.RecordBatch]:
    while True:
        try:
            yield reader.read_next_batch()
        except StopIteration:
            return
