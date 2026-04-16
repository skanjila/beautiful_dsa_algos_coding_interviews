from beautiful_dsa_algos_coding_interviews.dp.word_break import word_break


def test_word_break_true():
    assert word_break("leetcode", ["leet", "code"]) is True


def test_word_break_false():
    assert word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False
