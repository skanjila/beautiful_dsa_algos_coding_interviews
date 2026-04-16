from beautiful_dsa_algos_coding_interviews.hashing.valid_anagram import is_anagram


def test_valid_anagram_true():
    assert is_anagram("anagram", "nagaram") is True


def test_valid_anagram_false():
    assert is_anagram("rat", "car") is False
