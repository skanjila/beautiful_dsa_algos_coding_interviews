from typing import List, Set


def word_break(s: str, word_dict: List[str]) -> bool:
    """
    Return whether ``s`` can be segmented into dictionary words.

    ``dp[i]`` means the prefix ``s[:i]`` is segmentable. Each true position
    tries to extend forward using dictionary matches.

    Time complexity: O(N^2) in the common analysis
    Space complexity: O(N)
    """

    words: Set[str] = set(word_dict)
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for end in range(1, len(s) + 1):
        for start in range(end):
            # If the prefix up to ``start`` is valid and the slice ``start:end``
            # is a dictionary word, then the prefix up to ``end`` is valid too.
            if dp[start] and s[start:end] in words:
                dp[end] = True
                break

    return dp[len(s)]
