from dsa_practice.backtracking.combination_sum import combination_sum

def test_basic_combination_sum_happy_path_one():
    target = 6
    candidates = [1, 2, 3, 4, 5]
    got = combination_sum(candidates, target)

    # Expected combinations (each candidate used at most once)
    expected = [[1, 5], [2, 4], [1, 2, 3]]

    # Normalize: sort numbers inside each combo, and sort the list of combos
    normalize = lambda lst: sorted([sorted(x) for x in lst])

    assert normalize(got) == normalize(expected)


def test_basic_combination_sum_happy_path_two():
    target = 10
    candidates = [1, 2, 3, 4, 5, 7]
    got = combination_sum(candidates, target)

    # Expected combinations (each candidate used at most once)
    expected = [[1, 2, 7], [1, 2, 3, 4], [1, 4, 5], [2,3,5], [3,7]]

    # Normalize: sort numbers inside each combo, and sort the list of combos
    normalize = lambda lst: sorted([sorted(x) for x in lst])

    assert normalize(got) == normalize(expected)