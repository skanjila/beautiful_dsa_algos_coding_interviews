from typing import List


def longest_ones(nums: List[int], k: int = 0) -> int:
    """
    Finds the longest contiguous sequence of 1s in a binary array,
    allowing up to k flips of 0s to 1s (k=0 for pure consecutive 1s).

    Uses a sliding window to efficiently compute the result.

    Args:
        nums (List[int]): The binary input array.
        k (int): Maximum number of 0s allowed to flip. Default is 0 (no flips).

    Returns:
        int: The length of the longest contiguous sequence of 1s.
    """
    left = 0
    max_len = 0
    zero_count = 0

    for right in range(len(nums)):
        # Expand window by including nums[right]
        if nums[right] == 0:
            zero_count += 1

        # Shrink window if more than k zeros
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        # Update maximum length
        max_len = max(max_len, right - left + 1)

    return max_len
