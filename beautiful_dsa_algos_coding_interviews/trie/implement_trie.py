class TrieNode:
    """
    One trie node holding child pointers and an end-of-word marker.

    Time complexity: O(1) to construct.
    Space complexity: O(1) plus children stored later.
    """

    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    """
    Prefix tree supporting insert, exact search, and prefix search.

    Insert/search/starts_with all run in O(L) time where L is word length.
    Space complexity: O(total characters stored across inserted words).
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            # Walk one prefix character at a time, creating missing branches on demand.
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            # Exact search fails immediately if any required prefix edge is missing.
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            # Prefix search only cares that the path exists; it does not require
            # the final node to mark a completed word.
            if char not in node.children:
                return False
            node = node.children[char]
        return True
