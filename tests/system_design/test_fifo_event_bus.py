import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from system_design.implementations.fifo_event_bus import FIFOEventBus


def test_publish_preserves_fifo_order_within_a_partition() -> None:
    bus = FIFOEventBus()
    bus.create_topic("orders", partitions=3)

    first = bus.publish("orders", key="customer-1", value={"step": 1})
    second = bus.publish("orders", key="customer-1", value={"step": 2})

    assert first.partition == second.partition
    assert first.offset == 0
    assert second.offset == 1

    records = bus.read_from("orders", first.partition, offset=0, max_records=10)
    assert [record.value for record in records] == [{"step": 1}, {"step": 2}]


def test_consumer_group_commit_and_lag_tracking() -> None:
    bus = FIFOEventBus()
    bus.create_topic("notifications", partitions=2)

    first = bus.publish("notifications", key="user-1", value="welcome")
    bus.publish("notifications", key="user-1", value="follow-up")

    polled = bus.poll_group("email-workers", "notifications", first.partition, 10)
    assert [record.value for record in polled] == ["welcome", "follow-up"]
    assert bus.lag("email-workers", "notifications", first.partition) == 2

    bus.commit("email-workers", "notifications", first.partition, next_offset=1)

    remaining = bus.poll_group("email-workers", "notifications", first.partition, 10)
    assert [record.value for record in remaining] == ["follow-up"]
    assert bus.lag("email-workers", "notifications", first.partition) == 1


def test_invalid_offsets_and_duplicate_topics_raise_errors() -> None:
    bus = FIFOEventBus()
    bus.create_topic("events", partitions=1)

    try:
        bus.create_topic("events", partitions=1)
        assert False, "expected duplicate topic creation to fail"
    except ValueError:
        pass

    bus.publish("events", key="entity-1", value="created")

    try:
        bus.commit("workers", "events", 0, next_offset=2)
        assert False, "expected invalid commit offset to fail"
    except ValueError:
        pass
