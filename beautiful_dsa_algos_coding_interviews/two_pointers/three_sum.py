from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Finds all unique triplets in the array which give the sum of zero.

    Pattern: Sorting + Two Pointers
    Time Complexity: O(n^2)
    Space Complexity: O(1) (excluding output list)
    """
    nums.sort()  # Sort for duplicate handling and two-pointer movement
    n = len(nums)
    result = []

    for i in range(n):
        # Skip duplicate 'a' values
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1
        target = -nums[i]

        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])

                # Move left and right to the next distinct elements
                left_val, right_val = nums[left], nums[right]
                while left < right and nums[left] == left_val:
                    left += 1
                while left < right and nums[right] == right_val:
                    right -= 1

            elif current_sum < target:
                left += 1  # Need a larger sum
            else:
                right -= 1  # Need a smaller sum

    return result
