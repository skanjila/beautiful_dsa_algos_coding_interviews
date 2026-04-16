from typing import List


def three_sum_bf(nums: List[int]) -> List[List[int]]:
    """
    Brute-force reference implementation for 3Sum.

    Time complexity: O(N^3)
    Space complexity: O(K) for the set of unique triplets, where K is the
    number of zero-sum triplets found.
    """

    found = set()
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    found.add(tuple(sorted((nums[i], nums[j], nums[k]))))
    return [list(triplet) for triplet in sorted(found)]
