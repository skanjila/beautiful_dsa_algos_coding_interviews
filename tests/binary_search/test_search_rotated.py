import pytest

from beautiful_dsa_algos_coding_interviews.binary_search.search_in_rotated_array import search_rotated

@pytest.mark.parametrize(
    "nums,target,expected",
    [
        # No rotation (plain binary search cases)
        ([1,2,3,4,5,6,7], 1, 0),
        ([1,2,3,4,5,6,7], 4, 3),
        ([1,2,3,4,5,6,7], 7, 6),

        # Rotated in the middle
        ([4,5,6,7,0,1,2], 0, 4),
        ([4,5,6,7,0,1,2], 4, 0),
        ([4,5,6,7,0,1,2], 2, 6),
        ([6,7,0,1,2,3,4], 3, 5),

        # Rotated by one
        ([7,1,2,3,4,5,6], 7, 0),
        ([7,1,2,3,4,5,6], 1, 1),

        # Single element
        ([5], 5, 0),

        # Two elements rotated
        ([2,1], 1, 1),
        ([2,1], 2, 0),
    ],
)
def test_found_cases(nums, target, expected):
    assert search_rotated(nums, target) == expected


@pytest.mark.parametrize(
    "nums,target",
    [
        ([], 1),                         # empty
        ([1], 2),                        # single, not found
        ([4,5,6,7,0,1,2], 3),            # absent in rotated
        ([7,1,2,3,4,5,6], 8),            # out of range
        ([3,4,5,6,7,0,1,2], -1),         # below range
    ],
)
def test_not_found_cases(nums, target):
    assert search_rotated(nums, target) == -1


def test_all_rotations_consistency():
    """Optional: sanity check the function across all rotations."""
    base = [1,2,3,4,5,6,7]
    for k in range(len(base)):
        nums = base[k:] + base[:k]  # rotate by k
        for i, val in enumerate(base):
            idx = search_rotated(nums, val)
            # Verify that the value at returned index matches and exists.
            assert 0 <= idx < len(nums)
            assert nums[idx] == val
