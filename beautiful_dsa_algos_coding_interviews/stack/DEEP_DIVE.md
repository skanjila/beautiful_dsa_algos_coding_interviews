# Stack Deep Dive

Stack problems usually appear when the rule depends on the most recent
unresolved item.

Common interview shapes:

- delimiter matching
- postfix expression evaluation
- nested decoding or parsing
- path simplification
- rolling minimum or maximum with auxiliary stack state

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

- time: `O(N)` because each character is read once and each bracket can only be
  pushed and popped one time.
- space: `O(N)` worst case because an input made entirely of opening delimiters
  forces the stack to hold all of them at once.

## `edge_cases`

The wrapper makes empty-string and null behavior explicit before delegating to
the main stack-based validator.

## `min_stack`

Stack with constant-time minimum retrieval.

- Keep a second stack of running minima.
- Interview approach: if the question asks for normal stack operations plus one
  aggregate like min, store the aggregate alongside the normal structure.
- Big O: `O(1)` for all operations, `O(N)` space.

## `evaluate_reverse_polish_notation`

Evaluates postfix expressions.

- Push operands and reduce whenever an operator appears.
- Interview approach: postfix notation almost always means stack.
- Big O: `O(N)` time, `O(N)` space in the worst case.

## `decode_string`

Decodes nested repetition expressions such as `3[a2[c]]`.

- Use stacks to save the outer string context and repeat counts.
- Interview approach: nested structure plus "resume previous partial result"
  is a strong stack signal.
- Big O: input scan is linear, with additional work proportional to output size.

## `simplify_path`

Normalizes Unix-style paths.

- Keep only meaningful path segments and pop when `..` appears.
- Interview approach: path backtracking maps naturally to stack pop operations.
- Big O: `O(N)` time, `O(N)` space.
