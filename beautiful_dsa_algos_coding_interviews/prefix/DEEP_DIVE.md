# Prefix Deep Dive

## `product_array_except_self`

Computes the product of all elements except the current index without using division.

### Core idea

- Forward pass stores the product of everything to the left.
- Backward pass multiplies in the product of everything to the right.

### Interview approach

If the interviewer bans division, think "prefix work from the left, suffix work
from the right". This is the standard move for array problems where each output
depends on everything except one index.

This is a classic prefix/suffix accumulation problem.

### Big O

- time: `O(N)` because the algorithm makes one forward pass to write left
  products and one backward pass to multiply in right products, so each index is
  touched a constant number of times.
- auxiliary space: `O(1)` excluding output because the running prefix and
  suffix products are held in scalar variables rather than separate arrays.

## `edge_cases`

The wrapper handles empty arrays and singleton arrays explicitly, then delegates
to the main `O(N)` implementation.
