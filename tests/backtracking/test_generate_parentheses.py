from beautiful_dsa_algos_coding_interviews.backtracking.generate_parentheses import (
    generate_parentheses,
)


def test_generate_parentheses_zero_pairs():
    assert generate_parentheses(0) == [""]


def test_generate_parentheses_one_pair():
    assert generate_parentheses(1) == ["()"]


def test_generate_parentheses_three_pairs():
    expected = {"((()))", "(()())", "(())()", "()(())", "()()()"}
    assert set(generate_parentheses(3)) == expected
