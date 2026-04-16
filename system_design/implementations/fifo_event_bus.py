"""A small Kafka-like event bus model for interview study and testing."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class EventRecord:
    topic: str
    partition: int
    offset: int
    key: str
    value: object


class FIFOEventBus:
    """Partitioned append-only log with consumer group offsets.

    This models the part of Kafka that interviewers usually care about:
    - messages are appended to a topic partition in order
    - ordering is guaranteed inside a partition, not across all partitions
    - consumers track offsets so they can resume from where they left off
    """

    def __init__(self) -> None:
        self._topics: dict[str, list[list[EventRecord]]] = {}
        self._committed_offsets: dict[str, dict[str, dict[int, int]]] = {}

    def create_topic(self, topic: str, partitions: int) -> None:
        if partitions <= 0:
            raise ValueError("partitions must be positive")
        if topic in self._topics:
            raise ValueError(f"topic already exists: {topic}")

        self._topics[topic] = [[] for _ in range(partitions)]

    def publish(self, topic: str, key: str, value: object) -> EventRecord:
        partitions = self._topics.get(topic)
        if partitions is None:
            raise KeyError(f"unknown topic: {topic}")

        partition = self._partition_for_key(key, len(partitions))
        log = partitions[partition]
        record = EventRecord(
            topic=topic,
            partition=partition,
            offset=len(log),
            key=key,
            value=value,
        )
        log.append(record)
        return record

    def read_from(
        self,
        topic: str,
        partition: int,
        offset: int,
        max_records: int = 10,
    ) -> list[EventRecord]:
        log = self._log_for_partition(topic, partition)
        return log[offset : offset + max_records]

    def poll_group(
        self,
        group: str,
        topic: str,
        partition: int,
        max_records: int = 10,
    ) -> list[EventRecord]:
        offset = self.committed_offset(group, topic, partition)
        return self.read_from(topic, partition, offset, max_records)

    def commit(self, group: str, topic: str, partition: int, next_offset: int) -> None:
        log = self._log_for_partition(topic, partition)
        if next_offset < 0 or next_offset > len(log):
            raise ValueError("next_offset is out of range")

        group_offsets = self._committed_offsets.setdefault(group, {})
        topic_offsets = group_offsets.setdefault(topic, {})
        topic_offsets[partition] = next_offset

    def committed_offset(self, group: str, topic: str, partition: int) -> int:
        return (
            self._committed_offsets.get(group, {})
            .get(topic, {})
            .get(partition, 0)
        )

    def lag(self, group: str, topic: str, partition: int) -> int:
        log = self._log_for_partition(topic, partition)
        return len(log) - self.committed_offset(group, topic, partition)

    def topic_partition_count(self, topic: str) -> int:
        partitions = self._topics.get(topic)
        if partitions is None:
            raise KeyError(f"unknown topic: {topic}")
        return len(partitions)

    def _log_for_partition(self, topic: str, partition: int) -> list[EventRecord]:
        partitions = self._topics.get(topic)
        if partitions is None:
            raise KeyError(f"unknown topic: {topic}")
        if partition < 0 or partition >= len(partitions):
            raise IndexError("partition out of range")
        return partitions[partition]

    @staticmethod
    def _partition_for_key(key: str, partition_count: int) -> int:
        # The deterministic sum keeps tests stable across Python processes,
        # unlike the built-in hash function which is intentionally randomized.
        return sum(ord(char) for char in key) % partition_count
