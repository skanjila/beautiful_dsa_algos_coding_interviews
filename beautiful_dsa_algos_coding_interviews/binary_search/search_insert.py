from typing import List


def search_insert(nums: List[int], target: int) -> int:
    """
    Return the index where ``target`` exists or should be inserted.

    The input is assumed to already be sorted in ascending order. We keep
    shrinking the candidate range until ``left`` points at the first index whose
    value is not smaller than ``target``. If every value is smaller, ``left``
    naturally ends at ``len(nums)``, which is the correct append position.

    Time complexity: O(log N)
    Space complexity: O(1)
    """

    left, right = 0, len(nums) - 1

    # The invariant is:
    # - every index strictly before ``left`` contains a value < target
    # - every index strictly after ``right`` contains a value >= target
    # When the loop finishes, ``left`` is the only valid insertion position.
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # If the middle value is too small, the answer must be to the right of
        # ``mid`` because a sorted array cannot contain the insertion point on
        # the left side anymore.
        if nums[mid] < target:
            left = mid + 1
        else:
            # Otherwise ``mid`` itself could still be the insertion point, so we
            # keep the left half and discard only the larger right half.
            right = mid - 1

    return left
