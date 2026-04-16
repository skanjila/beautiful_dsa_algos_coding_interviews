from beautiful_dsa_algos_coding_interviews.heap.kth_largest_element import kth_largest
from beautiful_dsa_algos_coding_interviews.heap.top_k_frequent import top_k_frequent


def test_kth_largest():
    assert kth_largest([3, 2, 1, 5, 6, 4], 2) == 5


def test_top_k_frequent():
    assert top_k_frequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
