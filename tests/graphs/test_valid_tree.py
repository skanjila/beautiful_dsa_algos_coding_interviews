from beautiful_dsa_algos_coding_interviews.graphs.valid_tree import valid_tree


def test_valid_tree_true_case():
    assert valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) is True


def test_valid_tree_false_cycle_case():
    assert valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) is False
