from typing import List


def _binary_boundary(nums: List[int], target: int, find_first: bool) -> int:
    """
    Locate either boundary index for ``target`` in a sorted array.

    ``find_first=True`` keeps walking left after a match to find the earliest
    occurrence. ``find_first=False`` walks right to find the latest occurrence.
    If the target never appears, ``boundary`` stays ``-1``.

    Time complexity: O(log N)
    Space complexity: O(1)
    """

    left, right = 0, len(nums) - 1
    boundary = -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            boundary = mid

            # We found the target, but not necessarily the boundary we want.
            # Keep searching only the side that could still contain an earlier
            # or later copy of the same value.
            if find_first:
                right = mid - 1
            else:
                left = mid + 1

    return boundary


def search_range(nums: List[int], target: int) -> List[int]:
    """
    Return the first and last index of ``target`` inside a sorted array.

    The algorithm performs two binary searches instead of one linear scan:
    one for the left boundary and one for the right boundary. That preserves
    ``O(log n)`` time even when the target occurs many times.

    Time complexity: O(log N)
    Space complexity: O(1)
    """

    first = _binary_boundary(nums, target, find_first=True)
    if first == -1:
        return [-1, -1]

    last = _binary_boundary(nums, target, find_first=False)
    return [first, last]
