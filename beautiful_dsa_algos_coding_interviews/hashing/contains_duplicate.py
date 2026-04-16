from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    """
    Return whether any value appears more than once.

    Time complexity: O(N) because each number is checked once against a hash set.
    Space complexity: O(N) in the worst case when all values are distinct.
    """
    seen = set()
    for value in nums:
        if value in seen:
            return True
        seen.add(value)
    return False
