import pytest
from beautiful_dsa_algos_coding_interviews.sliding_window.length_of_longest_substring import length_of_longest_substring

@pytest.mark.parametrize(
    "s, expected",
    [
        ("", 0),
        ("a", 1),
        ("abcde", 5),
        ("bbbbb", 1),
        ("abcabcbb", 3),
        ("pwwkew", 3),
        ("dvdf", 3),
        ("abba", 2),
        ("tmmzuxt", 5),
        ("anviaj", 5),
        ("这里有中文", 5),
        ("😀😃😄😁😆😅😂🤣", 8),
        ("😀a😀b😀c", 3),
    ],
)
def test_length_of_longest_substring_param(s, expected):
    assert length_of_longest_substring(s) == expected


def test_long_repeats_pattern():
    s = "abc" * 1000
    assert length_of_longest_substring(s) == 3


def test_increasing_then_repeat():
    assert length_of_longest_substring("abcdefga") == 7
