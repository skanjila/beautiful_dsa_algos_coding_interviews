from beautiful_dsa_algos_coding_interviews.strings.string_to_integer_atoi import string_to_integer


def test_string_to_integer_basic():
    assert string_to_integer("   -42") == -42


def test_string_to_integer_clamps():
    assert string_to_integer("91283472332") == 2147483647
