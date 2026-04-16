# Beautiful DSA Algos Coding Interviews

This repo is an interview-prep workspace that combines:

- executable data structures and algorithms implementations
- tests for the implementations
- deep-dive markdown guides for major DSA pattern families
- study modules for system design, data engineering, and data science

It is designed to be used as a study repo first and a Python codebase second.

## Repo Layout

### Core DSA code

The main Python implementations live in:

- [beautiful_dsa_algos_coding_interviews](/Users/skanjilal/employment/code/beautiful_dsa_algos_coding_interviews/beautiful_dsa_algos_coding_interviews)

This package contains directories for major interview patterns and problem types:

- `backtracking`
- `binary_search`
- `dp`
- `graphs`
- `hashing`
- `heap`
- `intervals`
- `linked_list`
- `math`
- `monotonic_stack`
- `multi_ds`
- `prefix`
- `search/bfs`
- `search/dfs`
- `sliding_window`
- `stack`
- `strings`
- `trees/binary_tree`
- `trie`
- `two_pointers`
- `union_find`

Most directories contain:

- Python implementations
- optional edge-case wrapper modules
- a `DEEP_DIVE.md` study guide

### Tests

Tests live in:

- [tests](/Users/skanjilal/employment/code/beautiful_dsa_algos_coding_interviews/tests)

### Study modules

These are structured interview-prep directories at the repo root:

- [system_design](/Users/skanjilal/employment/code/beautiful_dsa_algos_coding_interviews/system_design)
- [data_engineering](/Users/skanjilal/employment/code/beautiful_dsa_algos_coding_interviews/data_engineering)
- [data_science](/Users/skanjilal/employment/code/beautiful_dsa_algos_coding_interviews/data_science)

### General docs

- [docs](/Users/skanjilal/employment/code/beautiful_dsa_algos_coding_interviews/docs)

## How To Run The Tests

This repo currently uses the root virtual environment at:

- `/Users/skanjilal/employment/code/newenv`

Run the full test suite:

```bash
/Users/skanjilal/employment/code/newenv/bin/python -m pytest /Users/skanjilal/employment/code/beautiful_dsa_algos_coding_interviews/tests -q
```

Run one test directory:

```bash
/Users/skanjilal/employment/code/newenv/bin/python -m pytest /Users/skanjilal/employment/code/beautiful_dsa_algos_coding_interviews/tests/backtracking -q
```

Run one test file:

```bash
/Users/skanjilal/employment/code/newenv/bin/python -m pytest /Users/skanjilal/employment/code/beautiful_dsa_algos_coding_interviews/tests/search/dfs/test_number_of_islands.py -q
```

## How To Use The Code

If you want to import an implementation directly, run from the repo root and use:

```python
from beautiful_dsa_algos_coding_interviews.binary_search.search_insert import search_insert

print(search_insert([1, 3, 5, 6], 2))
```

You can also use the interview study modules directly:

```python
from system_design.question_bank import search_questions

for item in search_questions("cache"):
    print(item.question)
```

## How To Get The Most Value Out Of This Repo

The best way to use this repo is not to read it linearly.

### Recommended DSA workflow

1. Pick one pattern family.
   Examples: sliding window, binary search, DFS, monotonic stack.
2. Read that directory’s `DEEP_DIVE.md`.
3. Open one implementation and trace the code comments line by line.
4. Run the matching test file.
5. Re-implement the solution from memory.
6. Compare your version to the repo version and its comments.

Good places to start:

- [sliding_window/DEEP_DIVE.md](/Users/skanjilal/employment/code/beautiful_dsa_algos_coding_interviews/beautiful_dsa_algos_coding_interviews/sliding_window/DEEP_DIVE.md)
- [binary_search/DEEP_DIVE.md](/Users/skanjilal/employment/code/beautiful_dsa_algos_coding_interviews/beautiful_dsa_algos_coding_interviews/binary_search/DEEP_DIVE.md)
- [search/dfs/DEEP_DIVE.md](/Users/skanjilal/employment/code/beautiful_dsa_algos_coding_interviews/beautiful_dsa_algos_coding_interviews/search/dfs/DEEP_DIVE.md)
- [two_pointers/DEEP_DIVE.md](/Users/skanjilal/employment/code/beautiful_dsa_algos_coding_interviews/beautiful_dsa_algos_coding_interviews/two_pointers/DEEP_DIVE.md)

### Recommended interview-prep workflow

Use the repo in layers:

1. Code layer:
   Learn the actual implementation mechanics and Big O.
2. Deep-dive layer:
   Learn pattern recognition, invariants, and interview framing.
3. Question-bank layer:
   Practice system design, data engineering, and data science interview answers.

That combination is the main value of the repo: it is not just code and it is
not just notes.

### For system design prep

Start with:

- [system_design/README.md](/Users/skanjilal/employment/code/beautiful_dsa_algos_coding_interviews/system_design/README.md)
- [system_design/interview_walkthrough.md](/Users/skanjilal/employment/code/beautiful_dsa_algos_coding_interviews/system_design/interview_walkthrough.md)

### For data engineering prep

Start with:

- [data_engineering/README.md](/Users/skanjilal/employment/code/beautiful_dsa_algos_coding_interviews/data_engineering/README.md)
- [data_engineering/practical_problems.md](/Users/skanjilal/employment/code/beautiful_dsa_algos_coding_interviews/data_engineering/practical_problems.md)

### For data science prep

Start with:

- [data_science/README.md](/Users/skanjilal/employment/code/beautiful_dsa_algos_coding_interviews/data_science/README.md)
- [data_science/interview_walkthrough.md](/Users/skanjilal/employment/code/beautiful_dsa_algos_coding_interviews/data_science/interview_walkthrough.md)

## What Makes This Repo Different

- The code includes inline interview-oriented comments, not just function bodies.
- The DSA directories include `DEEP_DIVE.md` guides, not just tests.
- The non-DSA study areas are structured and test-backed instead of being loose notes.
- Edge-case wrapper modules make interview boundary conditions explicit.

## Practical Advice

- Do not memorize final code blindly; memorize the pattern and invariant.
- Use the tests to validate your own rewrites.
- Use the markdown guides when you are learning the pattern.
- Use the code comments when you are trying to rebuild the solution under pressure.

## Current Baseline

At the time of writing, the repo test suite passes with:

```bash
/Users/skanjilal/employment/code/newenv/bin/python -m pytest /Users/skanjilal/employment/code/beautiful_dsa_algos_coding_interviews/tests -q
```
