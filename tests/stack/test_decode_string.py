from beautiful_dsa_algos_coding_interviews.stack.decode_string import decode_string


def test_decode_string_nested():
    assert decode_string("3[a2[c]]") == "accaccacc"


def test_decode_string_multiple_groups():
    assert decode_string("2[abc]3[cd]ef") == "abcabccdcdcdef"
