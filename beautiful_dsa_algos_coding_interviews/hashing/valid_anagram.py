def is_anagram(left: str, right: str) -> bool:
    """
    Check whether two strings contain the same character multiset.

    Time complexity: O(N) because each string is counted once.
    Space complexity: O(U) where U is the number of distinct characters stored.
    """
    if len(left) != len(right):
        return False

    counts = {}
    for char in left:
        counts[char] = counts.get(char, 0) + 1

    for char in right:
        if char not in counts:
            return False
        counts[char] -= 1
        if counts[char] == 0:
            del counts[char]

    return not counts
