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

- insert: `O(L)`
- search: `O(L)`
- starts_with: `O(L)`
- space: proportional to total stored characters
