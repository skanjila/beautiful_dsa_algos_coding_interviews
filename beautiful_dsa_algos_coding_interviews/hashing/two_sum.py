from typing import Dict, List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Return the indices of the two numbers that add up to ``target``.

    The standard interview solution uses a hash map from value to index so each
    element can ask whether its complement has already appeared.

    Time complexity: O(N)
    Space complexity: O(N)
    """

    seen: Dict[int, int] = {}

    for index, value in enumerate(nums):
        complement = target - value
        # The hash map stores numbers we've already passed, so if the complement
        # is present we can finish in one step without a nested loop.
        if complement in seen:
            return [seen[complement], index]
        # Save the current value after checking; this avoids using the same
        # element twice when target == 2 * value.
        seen[value] = index

    return []
