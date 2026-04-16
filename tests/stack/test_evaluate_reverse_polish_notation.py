from beautiful_dsa_algos_coding_interviews.stack.evaluate_reverse_polish_notation import eval_rpn


def test_eval_rpn_basic():
    assert eval_rpn(["2", "1", "+", "3", "*"]) == 9


def test_eval_rpn_division():
    assert eval_rpn(["4", "13", "5", "/", "+"]) == 6
