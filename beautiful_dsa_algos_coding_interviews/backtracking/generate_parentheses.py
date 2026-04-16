from typing import List


def generate_parentheses(n: int) -> List[str]:
    """
    Generate every well-formed parentheses string containing ``n`` pairs.

    Time complexity: O(C_n * n), where C_n is the nth Catalan number, because
    there are C_n valid strings and materializing each one costs O(n).
    Space complexity: O(n) recursion depth, excluding output.
    """

    if n < 0:
        return []

    results: List[str] = []

    def backtrack(open_count: int, close_count: int, path: List[str]) -> None:
        if len(path) == 2 * n:
            results.append("".join(path))
            return

        if open_count < n:
            path.append("(")
            backtrack(open_count + 1, close_count, path)
            path.pop()

        if close_count < open_count:
            path.append(")")
            backtrack(open_count, close_count + 1, path)
            path.pop()

    backtrack(0, 0, [])
    return results
