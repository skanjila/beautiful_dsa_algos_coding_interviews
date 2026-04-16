# Monotonic Stack Deep Dive

Monotonic stacks solve "next greater", "next smaller", and similar nearest
boundary problems in linear time.

## Interview Approach

Look for these phrases:

- next greater element
- next warmer day
- previous smaller
- nearest larger to the left or right

The calm idea is:

- keep indices in a stack whose values are monotonic
- when the current value breaks that monotonic condition, pop until it is restored
- each popped index has just found its answer

## `daily_temperatures`

Uses a decreasing stack of indices.

- When a warmer temperature appears, it resolves waiting colder days.
- Pattern to use quickly: next greater element on indices.
- Big O: `O(N)` time, `O(N)` space.

## `next_greater_element`

Returns the next greater value to the right for each position.

- Same monotonic pattern, but stores the greater value directly instead of a distance.
- Pattern to use quickly: classic next greater element.
- Big O: `O(N)` time, `O(N)` space.
