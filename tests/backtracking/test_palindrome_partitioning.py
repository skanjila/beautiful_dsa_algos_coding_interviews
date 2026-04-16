from beautiful_dsa_algos_coding_interviews.backtracking.palindrome_partitioning import (
    palindrome_partitioning,
)


def normalize(partitions):
    return sorted(tuple(partition) for partition in partitions)


def test_palindrome_partitioning_empty():
    assert palindrome_partitioning("") == [[]]


def test_palindrome_partitioning_aab():
    expected = [["a", "a", "b"], ["aa", "b"]]
    assert normalize(palindrome_partitioning("aab")) == normalize(expected)


def test_palindrome_partitioning_single_char():
    assert palindrome_partitioning("z") == [["z"]]
