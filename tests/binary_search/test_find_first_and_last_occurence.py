import pytest

from beautiful_dsa_algos_coding_interviews.binary_search.find_first_and_last_position import (
    search_range,
)


@pytest.mark.parametrize(
    "nums,target,expected",
    [
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ([5, 7, 7, 8, 8, 10], 7, [1, 2]),
        ([1], 1, [0, 0]),
        ([2, 2, 2, 2], 2, [0, 3]),
    ],
)
def test_search_range_basic_cases(nums, target, expected):
    assert search_range(nums, target) == expected


@pytest.mark.parametrize(
    "nums,target",
    [
        ([], 8),
        ([5, 7, 7, 8, 8, 10], 6),
        ([1], 0),
    ],
)
def test_search_range_missing_target(nums, target):
    assert search_range(nums, target) == [-1, -1]
