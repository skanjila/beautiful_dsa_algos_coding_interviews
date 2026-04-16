from typing import List

from beautiful_dsa_algos_coding_interviews.search.bfs.word_ladder import ladder_length


def ladder_length_with_edge_cases(begin_word: str, end_word: str, word_list: List[str]) -> int:
    """Guard wrapper for ``ladder_length``.

    Time complexity: O(M^2 * N) in the general case.
    Space complexity: Same as the wrapped function.
    """
    if not begin_word or not end_word:
        return 0
    if begin_word == end_word:
        return 1
    if not word_list:
        return 0
    return ladder_length(begin_word, end_word, word_list)
