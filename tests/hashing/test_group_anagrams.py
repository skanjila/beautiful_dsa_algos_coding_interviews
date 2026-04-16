from beautiful_dsa_algos_coding_interviews.hashing.group_anagrams import group_anagrams


def test_group_anagrams_basic():
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    normalized = sorted(sorted(group) for group in result)
    assert normalized == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
