import heapq
from typing import List


def kth_largest(nums: List[int], k: int) -> int:
    """
    Return the kth largest element using a size-k min-heap.

    Time complexity: O(N log K)
    Space complexity: O(K)
    """

    heap: List[int] = []
    for value in nums:
        heapq.heappush(heap, value)
        if len(heap) > k:
            # Keep only the k largest values seen so far; the smallest of those
            # k values sits at the heap root.
            heapq.heappop(heap)
    return heap[0]
