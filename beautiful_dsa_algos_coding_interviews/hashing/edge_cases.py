from typing import List

from beautiful_dsa_algos_coding_interviews.hashing.two_sum import two_sum


def two_sum_with_edge_cases(nums: List[int], target: int) -> List[int]:
    """
    Guard wrapper for ``two_sum``.

    Time complexity: O(N) for valid input.
    Space complexity: Same as the wrapped function.
    """

    if nums is None or len(nums) < 2:
        return []
    return two_sum(nums, target)
