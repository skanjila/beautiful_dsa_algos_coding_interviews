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

    # Initialize two pointers to define the current search range.
    left, right = 0, len(nums) - 1

    # Continue searching as long as the search range is valid.
    while left <= right:
        # Find the middle index of the current range.
        mid = (left + right) // 2

        # 🎯 Case 1: Found the target — return its index.
        if nums[mid] == target:
            return mid

        # ⚙️ Case 2: Determine which half of the array is sorted.
        # Remember, one of the halves (left or right) is guaranteed to be sorted.

        # If the LEFT half is sorted (i.e., nums[left] <= nums[mid]),
        # that means the rotation pivot is NOT in this segment.
        if nums[left] <= nums[mid]:
            # Check whether the target lies within this sorted left half.
            if nums[left] <= target <= nums[mid]:
                # If target is within this range, discard the right half.
                right = mid - 1
            else:
                # Otherwise, search in the right half.
                left = mid + 1

        # Otherwise, the RIGHT half must be sorted.
        else:
            # Check whether the target lies within this sorted right half.
            if nums[mid] <= target <= nums[right]:
                # If yes, move left pointer to narrow search to the right half.
                left = mid + 1
            else:
                # Otherwise, discard the right half and move to the left half.
                right = mid - 1

    # ❌ Target not found after searching all possible halves.
    return -1
