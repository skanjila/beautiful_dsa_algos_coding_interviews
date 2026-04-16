from typing import List

from beautiful_dsa_algos_coding_interviews.sliding_window.length_of_longest_substring import (
    length_of_longest_substring,
)
from beautiful_dsa_algos_coding_interviews.sliding_window.longest_ones import (
    longest_ones,
)


def length_of_longest_substring_with_edge_cases(s: str) -> int:
    """Guard wrapper for ``length_of_longest_substring``.

    Time complexity: O(N) for non-empty strings.
    Space complexity: Same as the wrapped function.
    """
    if not s:
        return 0
    return length_of_longest_substring(s)


def longest_ones_with_edge_cases(nums: List[int], k: int = 0) -> int:
    """Guard wrapper for ``longest_ones``.

    Time complexity: O(N) for non-empty arrays.
    Space complexity: Same as the wrapped function.
    """
    if not nums:
        return 0
    if k < 0:
        return 0
    return longest_ones(nums, k)
