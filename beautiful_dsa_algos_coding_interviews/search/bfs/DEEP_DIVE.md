# BFS Deep Dive

## `word_ladder`

Finds the shortest transformation length between two words when each step may
change exactly one character.

### Why BFS is the right pattern

Each valid word transformation is one edge with uniform cost. BFS explores by
distance layers, so the first time the destination is dequeued you have the
shortest path length.

### Interview approach

Under pressure, say this explicitly:

- words are nodes
- one-letter transformations are edges
- each edge costs one step
- shortest steps means BFS

That explanation is often half the battle in a graph interview.

### Implementation details

- Put all valid words into a set for `O(1)` membership checks.
- For each popped word, mutate every character position with all letters `a-z`.
- Add unseen valid words to the queue with `distance + 1`.

### Big O

- time: `O(M^2 * N)` in the common analysis
- space: `O(N)`

## `edge_cases`

The wrapper handles empty strings, identical start/end words, and empty word
lists before delegating to the BFS solver.
