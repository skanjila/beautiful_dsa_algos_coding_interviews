from typing import List


def search_rotated(nums: List[int], target: int) -> int:
    """
    Search for a target value in a rotated sorted array using binary search.

    A rotated sorted array is originally sorted but then rotated at some pivot.
    Example:
        [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

    We must find the target index in O(log n) time using modified binary search.

    Parameters:
        nums:   List[int] — the rotated sorted array
        target: int       — the value we are searching for

    Returns:
        Index of target if found, else -1

    Time complexity:  O(log n)
    Space complexity: O(1)
    """

    left, right = 0, len(nums) - 1

    # Each iteration discards half of the remaining range. The key twist is
    # that, in a rotated sorted array with distinct values, at least one side
    # of ``mid`` must still be normally sorted.
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # If the left endpoint is <= the middle value, the left half is in
        # sorted order and the rotation point, if any, must be on the right.
        if nums[left] <= nums[mid]:
            # Use strict ``< nums[mid]`` on the upper bound because equality was
            # already handled by the early return above.
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        else:
            # Symmetric case: the right half is normally sorted, so the decision
            # is based on whether the target falls inside that ordered interval.
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
