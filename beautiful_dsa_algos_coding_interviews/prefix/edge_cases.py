from typing import List

from beautiful_dsa_algos_coding_interviews.prefix.product_array_except_self import (
    product_except_self,
)


def product_except_self_with_edge_cases(nums: List[int]) -> List[int]:
    """Guard wrapper for ``product_except_self``.

    Time complexity: O(N) in the general case.
    Space complexity: O(1) auxiliary space, excluding output.
    """
    if not nums:
        return []
    if len(nums) == 1:
        return [1]
    return product_except_self(nums)
