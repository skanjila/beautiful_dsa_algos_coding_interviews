def longest_palindrome(s: str) -> str:
    """
    Return the longest palindromic SUBSTRING of s.

    Strategy:
      1) A palindrome mirrors around its center.
      2) For each index i, we try two centers:
         - Odd-length center at (i, i)
         - Even-length center at (i, i+1)
      3) Expand outward (left--, right++) while characters match.
      4) Track the best (longest) window we have seen so far.
    Time:  O(n^2) worst case (n centers * O(n) expansion in total)
    Space: O(1)
    """
    # Edge cases: empty or single-character strings are already palindromes
    if not s:
        return ""
    if len(s) == 1:
        return s

    def expand(left: int, right: int) -> tuple[int, int]:
        """
        Expand around a center between indices left and right.
        Preconditions:
          - If odd-length center: left == right
          - If even-length center: right == left + 1
        While the current window s[left..right] is a palindrome,
        we move left one step left and right one step right.

        IMPORTANT:
          When the while loop stops, we've gone ONE STEP TOO FAR.
          So the last valid palindrome is s[left+1 .. right-1].
        Returns:
          (start_index, end_index) of the MAX palindrome for this center.
          Both indices are inclusive.
        """
        # Expand as long as:
        #  1) we stay within bounds
        #  2) the characters at the ends match
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1      # try to grow on the left
            right += 1     # try to grow on the right

        # We stopped because either:
        #  - went out of bounds, or
        #  - found a mismatch
        # The last valid palindrome boundaries are one step back inside.
        return left + 1, right - 1

    # best_start/best_end define the inclusive range of the best palindrome so far
    best_start, best_end = 0, 0  # default to first char

    # Try every index as a potential center
    for i in range(len(s)):
        # 1) Odd-length palindrome centered at i (like 'aba')
        l1, r1 = expand(i, i)
        # If this palindrome is longer than what we have, record it
        if r1 - l1 > best_end - best_start:
            best_start, best_end = l1, r1

        # 2) Even-length palindrome centered between i and i+1 (like 'abba')
        l2, r2 = expand(i, i + 1)
        if r2 - l2 > best_end - best_start:
            best_start, best_end = l2, r2

    # Python slice end is exclusive, so use best_end + 1
    return s[best_start:best_end + 1]

def is_palindrome(s: str) -> bool:
    return s == s[::-1]


def brute_force_longest_pal_len(s: str) -> int:
    """
    Quadratic reference to verify that the returned palindrome
    is not only valid but also maximal length.
    """
    n = len(s)
    best = 0
    for i in range(n):
        for j in range(i, n):
            sub = s[i:j+1]
            if is_palindrome(sub):
                best = max(best, j - i + 1)
    return best