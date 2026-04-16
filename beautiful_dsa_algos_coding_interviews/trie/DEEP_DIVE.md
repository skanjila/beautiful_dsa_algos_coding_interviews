# Trie Deep Dive

Tries are prefix trees for string sets.

## Interview Approach

Reach for a trie when the problem is about:

- prefix lookup
- auto-complete
- dictionary search with many repeated prefixes
- efficient word/prefix insertion and query

The key insight is that many strings share prefixes, so a tree can avoid
repeating those prefixes over and over.

## `implement_trie`

Provides:

- `insert`
- `search`
- `starts_with`

Pattern to use quickly:

- each character is one edge
- each node represents one prefix
- `is_word` marks complete words

Big O:

- insert: `O(L)` because inserting a word follows or creates one trie edge per
  character in that word.
- search: `O(L)` because lookup walks one edge per character until a mismatch or
  the word ends.
- starts_with: `O(L)` for the same reason as search: it only needs to traverse
  the prefix characters.
- space: proportional to total stored characters
