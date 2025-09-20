import itertools
import math

from beautiful_dsa_algos_coding_interviews.strings.generate_anagrams import generate_anagrams


def test_empty_string():
    assert generate_anagrams("") == [""]

def test_single_char():
    assert generate_anagrams("a") == ["a"]

def test_unique_chars_count_and_membership():
    s = "abc"
    got = generate_anagrams(s)
    expected = sorted("".join(p) for p in itertools.permutations(s))
    assert got == expected
    assert len(got) == math.factorial(len(s))

def test_with_duplicates_unique_and_correct():
    s = "aab"
    got = generate_anagrams(s)
    # Expect exactly these three permutations
    expected = sorted({"aab", "aba", "baa"})
    assert got == expected
    # Ensure no duplicates
    assert len(got) == len(set(got))

def test_all_chars_same():
    s = "aaaa"
    got = generate_anagrams(s)
    assert got == ["aaaa"]  # only one unique permutation

def test_two_duplicates_pairwise():
    s = "aabb"
    got = generate_anagrams(s)
    # Cross-check against itertools unique perms
    expected = sorted(set("".join(p) for p in itertools.permutations(s)))
    assert got == expected
    assert len(got) == len(set(got))

def test_deterministic_ordering():
    # The function promises lexicographic order
    s = "bca"
    got = generate_anagrams(s)
    assert got == sorted(got)
