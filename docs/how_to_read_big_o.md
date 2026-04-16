# How To Read Big O In This Repo

This repo uses Big O constantly, but the intent is not to turn the material
into abstract math.

Use this translation:

- `N`: number of input items
- `M`: second input size, often word length or second array length
- `R * C`: rows times columns in a grid
- `V + E`: vertices plus edges in a graph
- `H`: tree height
- `W`: tree width
- `K`: window size, heap size, or output-group size depending on context

## The Main Question To Ask

Do not ask only:

- "What is the final formula?"

Ask:

- "What work is repeated?"
- "How many times can each element, node, or pointer move?"
- "What extra structure is being stored?"

That is how the explanations in the repo are intended to be read.

## Common Patterns

### `O(N)`

Read this as:

- every element is touched once
- or each element enters and leaves a data structure at most once

### `O(N log N)`

Read this as:

- there is a sort
- or there are `N` operations and each one costs `log N`

### `O(N^2)`

Read this as:

- there are two nested dimensions of work
- or one outer loop triggers a linear scan over the remaining elements

### `O(V + E)`

Read this as:

- every graph node is processed once
- every edge is inspected once

### `O(R * C)`

Read this as:

- each grid cell is visited once

### Exponential backtracking

Read this as:

- the algorithm explores a decision tree
- the real question is how many branches exist per step and how deep the tree goes

## Space Complexity

When the repo says `O(1)` auxiliary space, that usually means:

- the algorithm uses only a small fixed number of extra variables
- returned output is not being counted as auxiliary space

When the repo says `O(H)` or `O(W)` in trees, that usually means:

- `H`: recursion stack or explicit stack along one root-to-leaf path
- `W`: queue size for one level in BFS

## Best Way To Practice

After reading a complexity note, try to say it back in one sentence:

- "This is linear because every node is visited once."
- "This is `N log K` because I process all `N` items and each heap operation is logarithmic in heap size `K`."
- "This is exponential because I branch on many valid choices at each recursion level."

If you can say that sentence calmly, you understand the Big O well enough for
an interview.
