from collections import deque, defaultdict
from typing import List

def ladder_length(beginWord: str, endWord: str, wordList: List[str]) -> int:
    """Given two words beginWord and endWord, and a dictionary of words, return the length of the shortest
    transformation sequence from beginWord to endWord such that only one letter changes
     at a time and each intermediate word must exist in the dictionary.
    @param beginWord: The beginning of the word
    @param endWord: The end of the word
    """
    if endWord not in wordList:
        return 0
    L = len(beginWord)
    buckets = defaultdict(list)
    for w in wordList:
        for i in range(L):
            buckets[w[:i] + "*" + w[i+1:]].append(w)

    q = deque([(beginWord, 1)])
    visited = {beginWord}
    while q:
        word, dist = q.popleft()
        if word == endWord:
            return dist
        for i in range(L):
            pattern = word[:i] + "*" + word[i+1:]
            for nxt in buckets.get(pattern, []):
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, dist + 1))
            # Optional: clear to reduce future work
            buckets[pattern] = []
    return 0



