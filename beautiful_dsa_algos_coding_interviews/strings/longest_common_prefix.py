from typing import List


def longest_common_prefix(strings: List[str]) -> str:
    """
    Return the longest shared prefix across all strings.

    Time complexity: O(S) where S is the total number of compared characters,
    because each character is checked until the first mismatch.
    Space complexity: O(1) auxiliary excluding the returned prefix slice.
    """
    if not strings:
        return ""

    prefix = strings[0]
    for current in strings[1:]:
        while not current.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix
