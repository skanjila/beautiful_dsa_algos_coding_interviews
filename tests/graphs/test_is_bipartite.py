from beautiful_dsa_algos_coding_interviews.graphs.is_bipartite import is_bipartite


def test_is_bipartite_true_case():
    assert is_bipartite([[1, 3], [0, 2], [1, 3], [0, 2]]) is True


def test_is_bipartite_false_case():
    assert is_bipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]) is False
