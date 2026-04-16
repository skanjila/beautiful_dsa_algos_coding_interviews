from beautiful_dsa_algos_coding_interviews.backtracking.combination_sum import combination_sum
from beautiful_dsa_algos_coding_interviews.backtracking.combination_sum_ii import (
    combination_sum_ii,
)


def test_basic_combination_sum_ii_happy_path_one():
    target = 6
    candidates = [1, 2, 3, 4, 5]
    got = combination_sum_ii(candidates, target)

    # Expected combinations (each candidate used at most once)
    expected = [[1, 5], [2, 4], [1, 2, 3]]

    # Normalize: sort numbers inside each combo, and sort the list of combos
    normalize = lambda lst: sorted([sorted(x) for x in lst])

    assert normalize(got) == normalize(expected)


def test_basic_combination_sum_ii_happy_path_two():
    target = 10
    candidates = [1, 2, 3, 4, 5, 7]
    got = combination_sum_ii(candidates, target)

    # Expected combinations (each candidate used at most once)
    expected = [[1, 2, 7], [1, 2, 3, 4], [1, 4, 5], [2,3,5], [3,7]]

    # Normalize: sort numbers inside each combo, and sort the list of combos
    normalize = lambda lst: sorted([sorted(x) for x in lst])

    assert normalize(got) == normalize(expected)


def test_basic_combination_sum_allows_reuse():
    target = 7
    candidates = [2, 3, 6, 7]
    got = combination_sum(candidates, target)
    expected = [[2, 2, 3], [7]]

    normalize = lambda lst: sorted([sorted(x) for x in lst])
    assert normalize(got) == normalize(expected)


def test_combination_sum_deduplicates_repeated_candidates():
    got = combination_sum([2, 2, 3], 7)
    expected = [[2, 2, 3]]

    normalize = lambda lst: sorted([sorted(x) for x in lst])
    assert normalize(got) == normalize(expected)
