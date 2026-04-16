from typing import List

def product_except_self(nums: List[int]) -> List[int]:
    """
    Returns an array output where output[i] is equal to the
    product of all the elements of nums except nums[i].

    This version:
    - Avoids using division.
    - Runs in O(n) time because one forward pass writes left products and one
      backward pass multiplies in right products, so each index is touched a
      constant number of times.
    - Uses O(1) extra space excluding the output array because prefix and
      suffix products are tracked in scalar variables instead of helper arrays.

    Approach:
    1️⃣ Forward pass: compute prefix products (everything to the left of i).
    2️⃣ Backward pass: multiply by suffix products (everything to the right of i).
    """

    n = len(nums)
    if n == 0:
        return []

    result = [1] * n

    # Step 1: prefix products
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # Step 2: suffix products
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result
