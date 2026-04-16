import heapq
from collections import Counter
from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    Return the ``k`` most frequent values.

    Time complexity: O(N log K) because counting is one linear pass and then
    each distinct value may trigger a heap operation of cost log K.
    Space complexity: O(N) because the frequency map can hold every distinct
    value from the input.
    """

    counts = Counter(nums)
    heap: List[tuple[int, int]] = []

    for value, freq in counts.items():
        heapq.heappush(heap, (freq, value))
        if len(heap) > k:
            # Evict the weakest candidate so the heap only tracks the current
            # top-k frequencies instead of sorting the whole map.
            heapq.heappop(heap)

    return [value for _, value in sorted(heap, reverse=True)]
