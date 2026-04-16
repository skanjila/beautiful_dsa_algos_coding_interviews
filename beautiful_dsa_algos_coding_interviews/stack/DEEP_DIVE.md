# Stack Deep Dive

## `match_parenthesees`

Validates bracket matching using a stack.

### Core idea

- Opening delimiters are pushed.
- Closing delimiters must match the most recent unmatched opening delimiter.

### Interview approach

Whenever the problem says "most recent unmatched", "nested", or "balanced",
think stack. The mental shortcut is LIFO structure for nested constraints.

This is the standard LIFO pattern for balanced-bracket validation.

### Big O

- time: `O(N)`
- space: `O(N)` worst case when the string is all opening delimiters

## `edge_cases`

The wrapper makes empty-string and null behavior explicit before delegating to
the main stack-based validator.
