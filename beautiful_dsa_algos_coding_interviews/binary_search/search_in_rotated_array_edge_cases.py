from typing import List

from beautiful_dsa_algos_coding_interviews.binary_search.search_in_rotated_array import (
    search_rotated,
)


def search_rotated_with_edge_cases(nums: List[int], target: int) -> int:
    """
    Add explicit handling for tiny inputs, unrotated arrays, and duplicate-heavy
    cases that can weaken the usual sorted-half deduction.

    Time complexity: O(log N) for the standard path, with an O(N) fallback for
    duplicate-heavy ambiguous cases.
    Space complexity: O(1)
    """

    if not nums:
        return -1

    if len(nums) == 1:
        return 0 if nums[0] == target else -1

    if nums[0] < nums[-1]:
        # The array is already fully sorted, so the standard implementation is
        # effectively a normal binary search.
        return search_rotated(nums, target)

    if nums[0] == nums[-1]:
        # Duplicate-heavy rotations can make the "which side is sorted" check
        # ambiguous. Use a direct scan so the result is still correct.
        for index, value in enumerate(nums):
            if value == target:
                return index
        return -1

    return search_rotated(nums, target)
