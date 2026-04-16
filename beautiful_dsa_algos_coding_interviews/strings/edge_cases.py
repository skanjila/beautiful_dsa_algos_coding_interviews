from typing import List

from beautiful_dsa_algos_coding_interviews.strings.generate_anagrams import (
    generate_anagrams,
)
from beautiful_dsa_algos_coding_interviews.strings.longest_palindromic_substring import (
    longest_palindrome,
)


def generate_anagrams_with_edge_cases(input_str: str) -> List[str]:
    """Guard wrapper for ``generate_anagrams``.

    Time complexity: O(N * N!) for non-null input.
    Space complexity: Same as the wrapped function.
    """
    if input_str is None:
        return []
    return generate_anagrams(input_str)


def longest_palindrome_with_edge_cases(s: str) -> str:
    """Guard wrapper for ``longest_palindrome``.

    Time complexity: O(N^2) for non-null input.
    Space complexity: O(1) auxiliary, ignoring the returned substring.
    """
    if s is None:
        return ""
    return longest_palindrome(s)
