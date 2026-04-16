from beautiful_dsa_algos_coding_interviews.dp.coin_change import coin_change


def test_coin_change_basic():
    assert coin_change([1, 2, 5], 11) == 3


def test_coin_change_impossible():
    assert coin_change([2], 3) == -1


def test_coin_change_zero_amount():
    assert coin_change([1, 2, 5], 0) == 0
