from typing import List

from beautiful_dsa_algos_coding_interviews.binary_search.median_of_two_sorted_arrays import (
    median_two_sorted_merge,
)


def _median_of_sorted_array(nums: List[int]) -> float:
    """Return the median for a single already-sorted array.

    Time complexity: O(1)
    Space complexity: O(1)
    """

    mid = len(nums) // 2
    if len(nums) % 2 == 1:
        return float(nums[mid])
    return (nums[mid - 1] + nums[mid]) / 2.0


def median_two_sorted_with_edge_cases(
    first_array: List[int], second_array: List[int]
) -> float:
    """
    Handle empty-input shortcuts before using the merge-based implementation.

    This keeps the behavior explicit for the cases that are easy to answer
    without building a merged array.

    Time complexity: O(M + N) in the general case, with O(1) shortcuts for the
    smallest edge cases.
    Space complexity: O(M + N) in the general case.
    """

    if not first_array and not second_array:
        raise ValueError("Both input arrays are empty; median is undefined.")

    if not first_array:
        return _median_of_sorted_array(second_array)

    if not second_array:
        return _median_of_sorted_array(first_array)

    if len(first_array) == 1 and len(second_array) == 1:
        return (first_array[0] + second_array[0]) / 2.0

    return median_two_sorted_merge(first_array, second_array)
