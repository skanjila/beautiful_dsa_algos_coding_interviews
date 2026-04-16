# Section Index

This file is the high-level map of the repo so the study content stays easy to
follow.

## Core DSA Sections

- `two_pointers`
- `sliding_window`
- `hashing`
- `binary_search`
- `stack`
- `monotonic_stack`
- `prefix`
- `intervals`
- `linked_list`
- `heap`
- `trie`
- `union_find`
- `multi_ds`
- `search/bfs`
- `search/dfs`
- `trees/binary_tree`
- `backtracking`
- `graphs`
- `dp`
- `math`
- `strings`

## Interview Study Modules

- `system_design`
- `data_engineering`
- `data_science`
- `machine_learning_engineering`

## Intentional Variants, Not Accidental Duplicates

The repo does include a few deliberate variant pairs. These are kept because
they teach different patterns or provide brute-force baselines.

- `graphs/can_finish.py` and `graphs/can_finish_dfs.py`
  Same course-schedule problem, but one teaches Kahn's algorithm and the other
  teaches DFS cycle detection.
- `two_pointers/three_sum.py` and `two_pointers/three_sum_bf.py`
  Optimized versus brute-force baseline.
- `trees/binary_tree/right_side_view.py` and `trees/binary_tree/rightmost_node_binary_tree.py`
  Same interview shape. Keep one as the main reference and treat the other as a
  view-pattern variant.

## What Was Cleaned Up

- removed the stray `backtracking/_init__.py` file because it was not part of
  the actual package structure
- kept pattern variants where they help study different solution families

## Recommended Reading Order

See [study_guide_roadmap.md](/Users/skanjilal/employment/code/beautiful_dsa_algos_coding_interviews/docs/study_guide_roadmap.md).
