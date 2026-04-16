# Study Guide Roadmap

This roadmap is the recommended way to work through the repo so you become
strong across coding, ML, system design, and production-oriented interviews
instead of overfitting to one category.

## Phase 1: Core Coding Fluency

Goal: become fast at recognizing and implementing the most common DSA patterns.

Work in this order:

1. `two_pointers`
2. `sliding_window`
3. `hashing`
4. `binary_search`
5. `stack`
6. `monotonic_stack`
7. `prefix`
8. `intervals`

Why this order:

- these are common interview patterns
- they teach invariants clearly
- they give quick feedback loops
- they are easier to revisit repeatedly

How to work each section:

1. Read the directory `DEEP_DIVE.md`.
2. Re-implement one problem from memory.
3. Run the matching tests.
4. Review the code comments and complexity derivations.

## Phase 2: Recursion And Search

Goal: become comfortable choosing DFS, BFS, recursion, and backtracking calmly.

Work in this order:

1. `search/bfs`
2. `search/dfs`
3. `trees`
4. `backtracking`
5. `graphs`

Why this order:

- BFS and DFS are foundational search patterns
- tree recursion becomes easier after graph/grid DFS
- backtracking is easier once recursive state management feels natural
- graph problems become easier once traversal language is automatic

High-value problems to master here:

- `word_ladder`
- `number_of_islands`
- `clone_graph`
- `binary_tree_level_order`
- `lowest_common_ancestor`
- `path_sum_ii`
- `generate_parentheses`
- `word_search`
- `can_finish`
- `network_delay_time`

## Phase 3: Data Structures And Composite Patterns

Goal: get comfortable with the data-structure-heavy interview questions that
look harder at first glance but are mostly pattern recognition.

Work in this order:

1. `linked_list`
2. `heap`
3. `trie`
4. `union_find`
5. `multi_ds`

High-value problems:

- reverse linked list
- merge two sorted lists
- kth largest element
- top k frequent
- implement trie
- count components with union find
- LRU cache

## Phase 4: Dynamic Programming

Goal: get comfortable identifying overlapping subproblems and state
definitions without panicking.

Work in this order:

1. `dp`
2. revisit memoized graph/grid problems like `unique_paths`
3. revisit backtracking problems that can be contrasted with DP thinking

How to study DP here:

- define the state
- define the transition
- define the base cases
- explain the iteration or recursion order

## Phase 5: General System Design

Goal: be able to discuss scalable services with clean tradeoff reasoning.

Work in this order:

1. [system_design/README.md](/Users/skanjilal/employment/code/beautiful_dsa_algos_coding_interviews/system_design/README.md)
2. [system_design/interview_walkthrough.md](/Users/skanjilal/employment/code/beautiful_dsa_algos_coding_interviews/system_design/interview_walkthrough.md)
3. [docs/service_design.md](/Users/skanjilal/employment/code/beautiful_dsa_algos_coding_interviews/docs/service_design.md)
4. framework-specific docs:
   [docs/spring_service_design.md](/Users/skanjilal/employment/code/beautiful_dsa_algos_coding_interviews/docs/spring_service_design.md)
   and [docs/fastapi_service_design.md](/Users/skanjilal/employment/code/beautiful_dsa_algos_coding_interviews/docs/fastapi_service_design.md)

## Phase 6: Data Engineering And Data Science

Goal: be able to reason about data pipelines, features, evaluation, and model
quality under interview pressure.

Work in this order:

1. `data_engineering`
2. `data_science`

In data engineering, focus on:

- deduplication
- sessionization
- SCD Type 2
- incremental aggregation
- late-arriving data
- Spark versus Pandas reasoning

In data science, focus on:

- leakage
- feature engineering
- class imbalance
- calibration
- time-aware validation
- model choice and interpretation

## Phase 7: Machine Learning Engineering

Goal: connect coding, ML, and systems into one coherent interview skill set.

Work in this order:

1. [machine_learning_engineering/README.md](/Users/skanjilal/employment/code/beautiful_dsa_algos_coding_interviews/machine_learning_engineering/README.md)
2. [machine_learning_engineering/interview_walkthrough.md](/Users/skanjilal/employment/code/beautiful_dsa_algos_coding_interviews/machine_learning_engineering/interview_walkthrough.md)
3. [machine_learning_engineering/question_bank.py](/Users/skanjilal/employment/code/beautiful_dsa_algos_coding_interviews/machine_learning_engineering/question_bank.py)
4. [machine_learning_engineering/practical_question_bank.py](/Users/skanjilal/employment/code/beautiful_dsa_algos_coding_interviews/machine_learning_engineering/practical_question_bank.py)
5. [machine_learning_engineering/solutions.py](/Users/skanjilal/employment/code/beautiful_dsa_algos_coding_interviews/machine_learning_engineering/solutions.py)
6. [machine_learning_engineering/PRACTICE_PROBLEMS.md](/Users/skanjilal/employment/code/beautiful_dsa_algos_coding_interviews/machine_learning_engineering/PRACTICE_PROBLEMS.md)

Focus areas:

- ranking and recommendation
- search and retrieval
- feature stores and offline-online skew
- monitoring and retraining policy
- trust and safety systems
- LLM / RAG system reasoning

## Phase 8: Final Interview Loops

Goal: combine all layers into realistic practice.

Suggested weekly cycle:

1. 2 coding rounds
2. 1 SQL / DE round
3. 1 ML fundamentals round
4. 1 ML system design round
5. 1 general system design round
6. 1 review day for weak spots

## How To Avoid Getting Lost

- Do not jump randomly between distant sections every day.
- Use one primary section per session.
- Keep a small handwritten or local note of mistakes you repeat.
- Revisit solved problems after a few days, not immediately.

## How To Know You Are Ready

You are approaching strong readiness when you can:

- name the pattern quickly before coding
- explain Big O derivations without guessing
- solve medium coding problems from memory with clean invariants
- discuss data leakage and evaluation rigor naturally
- design a ranking or retrieval system in a structured way
- explain monitoring, drift, and launch risk clearly
