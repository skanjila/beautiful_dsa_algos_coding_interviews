import pytest
from typing import List

from beautiful_dsa_algos_coding_interviews.prefix.product_array_except_self import product_except_self


@pytest.mark.parametrize(
    "nums, expected",
    [
        # --- Basic cases ---
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([2, 3, 4, 5], [60, 40, 30, 24]),
        ([5, 1, 10], [10, 50, 5]),

        # --- Includes zero ---
        ([1, 2, 0, 4], [0, 0, 8, 0]),  # one zero → only position of zero gets nonzero
        ([0, 0, 3, 4], [0, 0, 0, 0]),  # two zeros → all outputs are zero

        # --- Single element ---
        ([7], [1]),  # conventionally, product except self = 1

        # --- Empty input ---
        ([], []),

        # --- Negative numbers ---
        ([-1, 2, -3, 4], [-24, 12, -8, 6]),
        ([-1, -2, -3, -4], [-24, -12, -8, -6]),
    ]
)
def test_product_except_self(nums: List[int], expected: List[int]):
    """
    Validates correctness of the product_except_self implementation
    across diverse inputs, including zeros and negatives.
    """
    assert product_except_self(nums) == expected


def test_large_input():
    """Stress test for large array to ensure O(n) scaling."""
    nums = [2] * 10000
    result = product_except_self(nums)
    assert len(result) == 10000
    # Each output = 2^(9999)
    assert all(x == 2 ** 9999 for x in result[:3])  # sample check


def test_consistency_with_manual_computation():
    """Brute-force cross-check on a small random list."""
    nums = [3, 5, 2]
    expected = []
    for i in range(len(nums)):
        prod = 1
        for j in range(len(nums)):
            if i != j:
                prod *= nums[j]
        expected.append(prod)
    assert product_except_self(nums) == expected
