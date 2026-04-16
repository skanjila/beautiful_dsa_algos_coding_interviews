from typing import List

from beautiful_dsa_algos_coding_interviews.two_pointers.is_palindrome import (
    is_palindrome,
)
from beautiful_dsa_algos_coding_interviews.two_pointers.three_sum import three_sum
from beautiful_dsa_algos_coding_interviews.two_pointers.three_sum_bf import three_sum_bf


def is_palindrome_with_edge_cases(s: str) -> bool:
    """Guard wrapper for ``is_palindrome``.

    Time complexity: O(N) for non-null input.
    Space complexity: Same as the wrapped function.
    """
    if s is None:
        return False
    return is_palindrome(s)


def three_sum_with_edge_cases(nums: List[int]) -> List[List[int]]:
    """Guard wrapper for ``three_sum``.

    Time complexity: O(N^2) for valid input.
    Space complexity: Same as the wrapped function.
    """
    if len(nums) < 3:
        return []
    return three_sum(nums)


def three_sum_bf_with_edge_cases(nums: List[int]) -> List[List[int]]:
    """Guard wrapper for ``three_sum_bf``.

    Time complexity: O(N^3) for valid input.
    Space complexity: Same as the wrapped function.
    """
    if len(nums) < 3:
        return []
    return three_sum_bf(nums)
