from collections import defaultdict
from typing import List


def group_anagrams(words: List[str]) -> List[List[str]]:
    """
    Group words that share the same sorted-character signature.

    Time complexity: O(N * K log K) because each of N words is sorted to build
    its signature, and sorting a word of length K costs K log K.
    Space complexity: O(N * K) because all words are stored in grouped buckets.
    """
    groups = defaultdict(list)
    for word in words:
        groups["".join(sorted(word))].append(word)
    return list(groups.values())
