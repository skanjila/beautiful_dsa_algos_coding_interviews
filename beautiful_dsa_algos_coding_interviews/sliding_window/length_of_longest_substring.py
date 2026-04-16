from typing import Dict

def length_of_longest_substring(s: str) -> int:
    """Return the longest substring with no repeated characters.

    Time complexity: O(N)
    Space complexity: O(min(N, alphabet_size))
    """
    last_seen: Dict[str, int] = {}  # ✅ real dict instance
    start = 0
    best = 0

    for i, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= start:
            start = last_seen[ch] + 1
        last_seen[ch] = i
        best = max(best, i - start + 1)

    return best
