from beautiful_dsa_algos_coding_interviews.monotonic_stack.daily_temperatures import (
    daily_temperatures,
)
from beautiful_dsa_algos_coding_interviews.monotonic_stack.next_greater_element import (
    next_greater_element,
)


def test_daily_temperatures():
    assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]


def test_next_greater_element():
    assert next_greater_element([2, 1, 2, 4, 3]) == [4, 2, 4, -1, -1]
