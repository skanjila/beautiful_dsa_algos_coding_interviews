from typing import List

from beautiful_dsa_algos_coding_interviews.binary_search.find_first_and_last_position import (
    search_range,
)


def search_range_with_edge_cases(nums: List[int], target: int) -> List[int]:
    """
    Cover empty arrays, singleton arrays, and obvious out-of-range values early.

    For non-trivial inputs we defer to the regular two-pass binary search.

    Time complexity: O(log N) in the non-trivial case after constant-time
    boundary checks.
    Space complexity: O(1)
    """

    if not nums:
        return [-1, -1]

    if len(nums) == 1:
        return [0, 0] if nums[0] == target else [-1, -1]

    if target < nums[0] or target > nums[-1]:
        return [-1, -1]

    if nums[0] == nums[-1] == target:
        return [0, len(nums) - 1]

    return search_range(nums, target)
