from collections import deque
from typing import List

def ladder_length(beginWord: str, endWord: str, wordList: List[str]) -> int:
    """
    Return the length of the shortest transformation sequence from beginWord to endWord.
    Change exactly one letter at a time, and every intermediate word must be in wordList.

    Simpler approach:
      - Put all words in a set for O(1) membership checks.
      - Standard BFS from beginWord.
      - For each word, try changing each character 'a'..'z' and push valid unseen words.

    Example:
      beginWord = "hit", endWord = "cog",
      wordList = ["hot","dot","dog","lot","log","cog"] -> 5 ("hit"→"hot"→"dot"→"dog"→"cog")
    """
    word_set = set(wordList)
    if endWord not in word_set:
        return 0  # impossible

    q = deque([(beginWord, 1)])  # (current_word, distance)
    visited = {beginWord}

    while q:
        word, dist = q.popleft()
        if word == endWord:
            return dist

        # Generate all 1-letter mutations of `word`
        word_chars = list(word)
        for i in range(len(word_chars)):
            original = word_chars[i]
            for c in "abcdefghijklmnopqrstuvwxyz":
                if c == original:
                    continue
                word_chars[i] = c
                candidate = "".join(word_chars)
                if candidate in word_set and candidate not in visited:
                    visited.add(candidate)
                    q.append((candidate, dist + 1))
            word_chars[i] = original  # restore

    return 0  # no path
