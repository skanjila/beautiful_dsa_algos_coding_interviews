# Heap Deep Dive

Heaps are the go-to pattern when you repeatedly need the smallest or largest
item while processing many candidates.

## Interview Approach

Ask:

- do I need only the top `k`, not a fully sorted list?
- do I repeatedly need the smallest or largest current element?
- can I keep a bounded heap instead of sorting everything?

Fast pattern map:

- kth largest / kth smallest -> size-k heap
- top k frequent -> frequency map + heap
- streaming median -> two heaps

## `kth_largest_element`

Uses a size-`k` min-heap.

- Keep only the `k` largest values seen so far.
- The root is the kth largest among them.
- Big O: `O(N log K)` time, `O(K)` space.

## `top_k_frequent`

Uses a frequency map and a size-`k` min-heap over `(frequency, value)` pairs.

- Count frequencies first.
- Keep only the `k` most frequent entries.
- Big O: `O(N log K)` time, `O(N)` space.
