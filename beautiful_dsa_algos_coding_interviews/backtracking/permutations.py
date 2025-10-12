from typing import List

def compute_permutations(nums: List[int]) -> List[List[int]]:
    """
    Generates all possible permutations of a given list of numbers using backtracking.

    Args:
        nums (List[int]): List of integers to permute.

    Returns:
        List[List[int]]: A list containing all possible permutations of the input list.
    """
    results = []        # Stores all the final permutations
    used = [False] * len(nums)  # Tracks which elements are already in the current path

    def backtrack(path: List[int]):
        # Base case: if the path length equals the input length → full permutation found
        if len(path) == len(nums):
            results.append(path[:])  # Append a copy of the current path
            return

        # Try adding each unused element to the path
        for i in range(len(nums)):
            if used[i]:
                continue  # Skip elements already used in this permutation

            # Choose
            used[i] = True
            path.append(nums[i])

            # Explore
            backtrack(path)

            # Un-choose (backtrack)
            path.pop()
            used[i] = False

    backtrack([])  # Start with an empty path
    return results
