from beautiful_dsa_algos_coding_interviews.union_find.count_components import (
    count_components,
)


def test_count_components():
    assert count_components(5, [[0, 1], [1, 2], [3, 4]]) == 2


def test_count_components_no_edges():
    assert count_components(3, []) == 3
