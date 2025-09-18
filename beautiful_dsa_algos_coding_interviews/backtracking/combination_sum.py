from typing import List


def combination_sum(candidates: List[int], target: int)-> List[List[int]]:
    """This function implements the combination sum algorithm by using backtracking.
    @param candidates: A list of candidate numbers.
    @param target: The target sum.
    @return: A list of all possible combinations."""

    candidates.sort()

    # define a result to store the combination sum
    results: List[List[int]] = []

    def backtrack(remaining_sum: int, comb_candidates: List[int], start_index: int) -> None:
        """A function that implements the backtracking algorithm that backtracks
        with the different combination of numbers adding up to the
        remaining sum."""
        if remaining_sum == 0:
            results.append(comb_candidates.copy())
            return
        elif remaining_sum < 0:
            return

        for i in range(start_index, len(candidates)):
            if i > start_index and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > remaining_sum:
                break
            comb_candidates.append(candidates[i])
            backtrack(remaining_sum - candidates[i], comb_candidates, i+1)
            comb_candidates.pop()

    backtrack(target, [], 0)

    return results
