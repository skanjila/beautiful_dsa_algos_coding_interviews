from typing import List


def subsets_fixed(nums: List[int]) -> List[List[int]]:
    """Return all unique subsets of nums (the power set).

    Time complexity: O(N * 2^N) because there are up to 2^N subsets and each
    copied subset can cost O(N).
    Space complexity: O(N) recursion depth, excluding output.
    """
    nums.sort()  # handle duplicates deterministically
    result: List[List[int]] = []

    def backtrack(start: int, path: List[int]) -> None:
        result.append(path.copy())
        for i in range(start, len(nums)):
            # skip duplicates at this depth
            if i > start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            backtrack(i + 1, path)  # advance with i+1 (NOT start+1)
            path.pop()

    backtrack(0, [])
    return result

def canon(lst):
    """Helper to normalize subset results (ignore ordering).

    Time complexity: O(K log K) over the normalized subset tuples.
    Space complexity: O(K) for the transformed collection.
    """
    return sorted([tuple(sorted(x)) for x in lst])
