# tests/graphs/test_ladder_length.py
import pytest

from beautiful_dsa_algos_coding_interviews.search.bfs.word_ladder import ladder_length

@pytest.mark.parametrize(
    "begin,end,word_list,expected",
    [
        ("a", "c", ["a", "b", "c"], 2),                 # a -> c (one step via pattern "*")
        ("aaa", "bbb", ["aab", "abb", "bbb"], 4),       # aaa->aab->abb->bbb
        ("aaa", "bbb", ["bbb"], 0),                     # unreachable: no intermediate bridges
        ("hit", "hog", ["hot", "hog"], 3),              # hit->hot->hog
        ("toon", "plea",
         ["poon","plee","same","poie","plie","poin","plea"], 7),  # classic example
    ],
)


def test_various_parametrized(begin, end, word_list, expected):
    assert ladder_length(begin, end, word_list) == expected