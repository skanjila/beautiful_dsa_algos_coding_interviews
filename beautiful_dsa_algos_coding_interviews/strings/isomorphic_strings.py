def is_isomorphic(s: str, t: str) -> bool:
    """
    Check whether characters from one string can map one-to-one onto the other.

    Time complexity: O(N) because the strings are scanned once in lockstep.
    Space complexity: O(U) where U is the number of distinct characters stored
    in the forward and reverse maps.
    """
    if len(s) != len(t):
        return False

    forward = {}
    reverse = {}

    for left, right in zip(s, t):
        if left in forward and forward[left] != right:
            return False
        if right in reverse and reverse[right] != left:
            return False
        forward[left] = right
        reverse[right] = left

    return True
