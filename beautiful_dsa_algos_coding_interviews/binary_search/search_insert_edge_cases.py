from typing import List

from beautiful_dsa_algos_coding_interviews.binary_search.search_insert import (
    search_insert,
)


def search_insert_with_edge_cases(nums: List[int], target: int) -> int:
    """
    Handle the obvious boundary cases before falling back to binary search.

    This version is useful when you want the intent around edge handling to be
    explicit in the code rather than inferred from the generic algorithm.

    Time complexity: O(log N) in the non-trivial case after constant-time
    boundary checks.
    Space complexity: O(1)
    """

    if not nums:
        return 0

    if target <= nums[0]:
        return 0

    if target > nums[-1]:
        return len(nums)

    if len(nums) == 1:
        return 0 if target <= nums[0] else 1

    return search_insert(nums, target)
