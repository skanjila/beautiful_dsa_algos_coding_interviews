from typing import List


def daily_temperatures(temperatures: List[int]) -> List[int]:
    """
    Return days until a warmer temperature for each day.

    Uses a decreasing monotonic stack of indices.

    Time complexity: O(N)
    Space complexity: O(N)
    """

    result = [0] * len(temperatures)
    stack: List[int] = []

    for index, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            # The current warmer day resolves every earlier colder day waiting
            # on the stack.
            prev_index = stack.pop()
            result[prev_index] = index - prev_index
        # Keep indices in decreasing-temperature order.
        stack.append(index)

    return result
