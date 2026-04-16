from typing import List


def palindrome_partitioning(s: str) -> List[List[str]]:
    """
    Partition ``s`` so every chosen substring is a palindrome.

    Time complexity: O(N * 2^N) in the worst case because the search explores
    exponentially many partitions and palindrome checks add linear work.
    Space complexity: O(N) recursion depth, excluding output.
    """

    results: List[List[str]] = []

    def is_palindrome(left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def backtrack(start: int, path: List[str]) -> None:
        if start == len(s):
            results.append(path.copy())
            return

        for end in range(start, len(s)):
            if not is_palindrome(start, end):
                continue
            path.append(s[start:end + 1])
            backtrack(end + 1, path)
            path.pop()

    if s == "":
        return [[]]

    backtrack(0, [])
    return results
