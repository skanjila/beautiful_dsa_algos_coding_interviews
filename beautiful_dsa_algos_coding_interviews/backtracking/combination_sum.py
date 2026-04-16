from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """
    Return all combinations whose numbers add to ``target``.

    This is the classic interview variant where each candidate may be reused
    any number of times. Sorting lets us prune once a candidate exceeds the
    remaining sum.

    Time complexity: Exponential in the search tree; commonly described as
    O(N^(T / M)) in the worst case, where N is the number of candidates,
    T is the target, and M is the smallest candidate.
    Space complexity: O(T / M) for the recursion path, excluding output.
    """

    sorted_candidates = sorted(set(candidates))
    results: List[List[int]] = []

    def backtrack(start_index: int, remaining_sum: int, path: List[int]) -> None:
        if remaining_sum == 0:
            results.append(path.copy())
            return

        for index in range(start_index, len(sorted_candidates)):
            candidate = sorted_candidates[index]
            if candidate > remaining_sum:
                break

            path.append(candidate)
            # Reuse is allowed, so stay on the same index instead of advancing.
            backtrack(index, remaining_sum - candidate, path)
            path.pop()

    if target < 0:
        return []

    backtrack(0, target, [])
    return results
