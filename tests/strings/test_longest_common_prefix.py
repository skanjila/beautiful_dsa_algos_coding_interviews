from beautiful_dsa_algos_coding_interviews.strings.longest_common_prefix import longest_common_prefix


def test_longest_common_prefix_basic():
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"


def test_longest_common_prefix_none():
    assert longest_common_prefix(["dog", "racecar", "car"]) == ""
