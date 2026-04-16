from beautiful_dsa_algos_coding_interviews.graphs.find_course_order import find_order


def test_find_course_order_returns_valid_order():
    order = find_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    assert order[0] == 0
    assert order[-1] == 3
    assert len(order) == 4


def test_find_course_order_cycle_returns_empty():
    assert find_order(2, [[1, 0], [0, 1]]) == []
