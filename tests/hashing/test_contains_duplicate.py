from beautiful_dsa_algos_coding_interviews.hashing.contains_duplicate import contains_duplicate


def test_contains_duplicate_true():
    assert contains_duplicate([1, 2, 3, 1]) is True


def test_contains_duplicate_false():
    assert contains_duplicate([1, 2, 3, 4]) is False
