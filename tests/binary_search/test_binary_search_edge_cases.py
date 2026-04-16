import pytest

from beautiful_dsa_algos_coding_interviews.binary_search.find_first_and_last_position import (
    search_range,
)
from beautiful_dsa_algos_coding_interviews.binary_search.find_first_and_last_position_edge_cases import (
    search_range_with_edge_cases,
)
from beautiful_dsa_algos_coding_interviews.binary_search.search_in_rotated_array import (
    search_rotated,
)
from beautiful_dsa_algos_coding_interviews.binary_search.search_in_rotated_array_edge_cases import (
    search_rotated_with_edge_cases,
)
from beautiful_dsa_algos_coding_interviews.binary_search.search_insert import search_insert
from beautiful_dsa_algos_coding_interviews.binary_search.search_insert_edge_cases import (
    search_insert_with_edge_cases,
)


@pytest.mark.parametrize(
    "nums,target,expected",
    [
        ([], 4, 0),
        ([1, 3, 3, 3, 5], 3, 2),
        ([1, 2, 4, 6], 5, 3),
        ([-10, -3, 0, 9], -11, 0),
    ],
)
def test_search_insert_edge_cases(nums, target, expected):
    assert search_insert(nums, target) == expected
    assert search_insert_with_edge_cases(nums, target) == expected


@pytest.mark.parametrize(
    "nums,target,expected",
    [
        ([], 1, -1),
        ([9], 9, 0),
        ([9], 3, -1),
        ([3, 1], 1, 1),
        ([5, 6, 7, 1, 2, 3, 4], 6, 1),
    ],
)
def test_search_rotated_edge_cases(nums, target, expected):
    assert search_rotated(nums, target) == expected
    assert search_rotated_with_edge_cases(nums, target) == expected


@pytest.mark.parametrize(
    "nums,target,expected",
    [
        ([], 1, [-1, -1]),
        ([1, 1, 1, 1], 1, [0, 3]),
        ([1, 2, 3, 4], 0, [-1, -1]),
        ([1, 2, 3, 4], 5, [-1, -1]),
        ([1, 2, 2, 2, 3, 4], 2, [1, 3]),
    ],
)
def test_search_range_edge_cases(nums, target, expected):
    assert search_range(nums, target) == expected
    assert search_range_with_edge_cases(nums, target) == expected


def test_search_rotated_with_edge_case_duplicates():
    nums = [2, 2, 2, 3, 4, 2]
    assert search_rotated_with_edge_cases(nums, 3) == 3
    assert search_rotated_with_edge_cases(nums, 9) == -1
