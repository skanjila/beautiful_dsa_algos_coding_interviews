# Linked List Deep Dive

Linked list questions reward pointer discipline more than clever math.

## Interview Approach

Say the pointers out loud before coding:

- what does `prev` point to?
- what does `current` point to?
- what node do I lose if I do not save `next` first?

For merge-style problems, use a dummy head early. It reduces branching and
keeps the pointer logic calm and linear.

## `list_node`

Basic singly linked-list node.

- Pattern role: shared building block for linked-list problems.
- Big O: `O(1)` construction.

## `reverse_linked_list`

Reverses the list by rewiring pointers one node at a time.

- Save `next`, point current node backward, then advance.
- Pattern to use quickly: iterative pointer reversal.
- Big O: `O(N)` time, `O(1)` space.

## `merge_two_sorted_lists`

Merges two already-sorted linked lists.

- Use a dummy head and attach the smaller current node each step.
- Pattern to use quickly: two-pointer merge, but on linked nodes rather than arrays.
- Big O: `O(M + N)` time, `O(1)` auxiliary space.
