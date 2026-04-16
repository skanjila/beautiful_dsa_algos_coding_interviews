from typing import List


def combination_sum_ii(candidates: List[int], target: int) -> List[List[int]]:
    """
    Return unique combinations that sum to ``target`` using each value at most once.

    This is the duplicate-aware interview variant often labeled Combination Sum II.

    Time complexity: O(2^N) in the worst case because each candidate can be
    chosen or skipped across the backtracking tree.
    Space complexity: O(N) for recursion depth, excluding output.
    """

    sorted_candidates = sorted(candidates)
    results: List[List[int]] = []

    def backtrack(start_index: int, remaining_sum: int, path: List[int]) -> None:
        if remaining_sum == 0:
            results.append(path.copy())
            return

        for index in range(start_index, len(sorted_candidates)):
            candidate = sorted_candidates[index]
            if index > start_index and candidate == sorted_candidates[index - 1]:
                continue
            if candidate > remaining_sum:
                break

            path.append(candidate)
            backtrack(index + 1, remaining_sum - candidate, path)
            path.pop()

    if target < 0:
        return []

    backtrack(0, target, [])
    return results
