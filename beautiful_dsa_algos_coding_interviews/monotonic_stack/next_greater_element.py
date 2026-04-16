from typing import List


def next_greater_element(nums: List[int]) -> List[int]:
    """
    Return the next greater element to the right for each position.

    Time complexity: O(N)
    Space complexity: O(N)
    """

    result = [-1] * len(nums)
    stack: List[int] = []

    for index, value in enumerate(nums):
        while stack and nums[stack[-1]] < value:
            # As soon as we see a larger value, it becomes the answer for every
            # smaller index waiting on the stack.
            prev_index = stack.pop()
            result[prev_index] = value
        # The stack remains decreasing by value.
        stack.append(index)

    return result
