from beautiful_dsa_algos_coding_interviews.strings.isomorphic_strings import is_isomorphic


def test_isomorphic_strings_true():
    assert is_isomorphic("egg", "add") is True


def test_isomorphic_strings_false():
    assert is_isomorphic("foo", "bar") is False
