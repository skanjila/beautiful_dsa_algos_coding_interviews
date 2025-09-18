# --- Run the user's three tests against the fixed function ---
from beautiful_dsa_algos_coding_interviews.backtracking.subsets import subsets_fixed


def canon(lst):
    """Helper to normalize subset results (ignore ordering)."""
    return sorted([tuple(sorted(x)) for x in lst])


def test_subsets_empty():
    nums = []
    expected = [[]]
    assert canon(subsets_fixed(nums)) == canon(expected)

def test_subsets_single_element():
    nums = [1]
    expected = [[], [1]]
    assert canon(subsets_fixed(nums)) == canon(expected)

def test_subsets_three_elements():
    nums = [1, 2, 3]
    expected = [
        [],
        [1], [2], [3],
        [1, 2], [1, 3], [2, 3],
        [1, 2, 3]
    ]
    assert canon(subsets_fixed(nums)) == canon(expected)