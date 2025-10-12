import pytest
from typing import List
from beautiful_dsa_algos_coding_interviews.backtracking.permutations import compute_permutations


# Helper to sort inner lists for easier comparison
def sort_permutations(perms: List[List[int]]) -> List[List[int]]:
    return sorted([sorted(p) for p in perms])


def test_permutations_basic():
    """Test that permutations of [1, 2, 3] are correct and complete."""
    nums = [1, 2, 3]
    result = compute_permutations(nums)

    # There should be 3! = 6 permutations
    assert len(result) == 6

    # Each permutation should be a unique ordering
    assert len(set(tuple(p) for p in result)) == 6

    # Check that all expected permutations are present
    expected = [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ]
    assert sorted(result) == sorted(expected)


def test_permutations_with_duplicates():
    """Test that input with duplicates generates duplicates in output (no deduplication logic)."""
    nums = [1, 1, 2]
    result = compute_permutations(nums)

    # There should be 3! = 6 total permutations (with duplicates)
    assert len(result) == 6

    # There will be only 3 unique permutations because of repeated 1s
    unique_perms = {tuple(p) for p in result}
    assert len(unique_perms) == 3
    assert {tuple(p) for p in unique_perms} == {(1, 1, 2), (1, 2, 1), (2, 1, 1)}


def test_single_element():
    """Test permutations of a single-element list."""
    nums = [42]
    result = compute_permutations(nums)
    assert result == [[42]]


def test_empty_input():
    """Test that an empty list returns a single empty permutation."""
    result = compute_permutations([])
    assert result == [[]]


def test_permutation_structure_integrity():
    """Ensure each permutation has same length as input and only valid elements."""
    nums = [1, 2, 3, 4]
    result = compute_permutations(nums)
    assert all(len(p) == len(nums) for p in result)
    assert all(set(p) == set(nums) for p in result)
