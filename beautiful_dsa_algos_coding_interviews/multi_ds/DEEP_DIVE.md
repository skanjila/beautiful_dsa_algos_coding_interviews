# Multi Data Structure Deep Dive

This directory focuses on problems that combine multiple structures.

## Interview Approach

When a problem demands two different operations to both be fast, ask whether one
data structure can answer one operation and another can answer the other.

For LRU cache specifically:

- hash map answers "find by key"
- linked list answers "who is oldest/newest"

That framing usually gets you to the canonical solution quickly.

## `lru_cache`

The cache combines:

- a dictionary for `O(1)` key lookup
- a doubly linked list for `O(1)` recency updates and eviction

### Why this combination works

The dictionary answers "where is the node for this key?" immediately. The list
answers "which node is least recently used?" immediately because the tail-side
node is the LRU entry.

### Operations

- `get`: dictionary lookup, then move the node to the front
- `put`: update existing node or insert a new one at the front
- `_evict_if_needed`: remove the node right before the tail when capacity is exceeded

### Big O

- `get`: `O(1)` amortized
- `put`: `O(1)` amortized
- space: `O(capacity)`
