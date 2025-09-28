import pytest
from typing import List

from beautiful_dsa_algos_coding_interviews.two_pointers.three_sum import three_sum


@pytest.mark.parametrize("nums, expected", [
    # Standard example
    ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),

    # Case with multiple duplicates
    ([0, 0, 0, 0], [[0, 0, 0]]),

    # Case with no valid triplets
    ([1, 2, 3, 4, 5], []),

    # Negative numbers only
    ([-5, -4, -3, -2, -1], []),

    # Positive numbers only
    ([1, 2, 3, 4], []),

    # Mixed with multiple triplets
    ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),

    # Just enough numbers but no zero-sum
    ([1, -1], []),

    # Large input with duplicates
    ([-2, -2, 0, 0, 2, 2], [[-2, 0, 2]]),

    # Single valid triplet at the edges
    ([-4, -1, -1, 0, 1, 2], [[-1, -1, 2], [-1, 0, 1]]),
])
def test_three_sum(nums: List[int], expected: List[List[int]]):
    result = three_sum(nums)

    # Since order of triplets and order inside triplets does not matter, normalize both
    normalize = lambda lst: sorted([sorted(triplet) for triplet in lst])
    assert normalize(result) == normalize(expected)
