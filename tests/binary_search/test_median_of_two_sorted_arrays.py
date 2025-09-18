import pytest
from dsa_practice.binary_search.median_of_two_sorted_arrays import median_two_sorted_merge

@pytest.mark.parametrize(
    "a,b,expected",
    [
        # Odd total length
        ([1, 3], [2], 2.0),
        ([1, 2, 3], [], 2.0),
        ([], [0, 0, 1], 0.0),
        ([-5, -1], [-3], -3.0),
        # Even total length
        ([1, 2], [3, 4], 2.5),
        ([1, 3], [2, 4], 2.5),
        ([0, 0], [0, 0], 0.0),
        ([1], [2, 3], 2.0),
        ([], [2, 2], 2.0),
        # Duplicates + overlaps
        ([1, 2, 2, 2], [2, 2, 3], 2.0),
        # Non-overlapping blocks
        ([1, 2, 3, 4], [100, 200], 3.5),
        # Negatives and positives
        ([-10, -2, -1], [0, 5, 9], -0.5),
    ],
)
def test_median_happy_paths(a, b, expected):
    assert median_two_sorted_merge(a, b) == pytest.approx(expected, rel=1e-12, abs=1e-12)

def test_raises_on_both_empty():
    with pytest.raises(ValueError):
        median_two_sorted_merge([], [])

def test_stability_when_equal_elements():
    # When equal, we take from the first array first; median should still be correct
    a = [1, 2, 2, 2, 3]
    b = [2, 2]
    # Combined: [1, 2, 2, 2, 2, 2, 3] -> median is 2
    assert median_two_sorted_merge(a, b) == 2.0

@pytest.mark.parametrize(
    "a,b",
    [
        ([1, 1, 1, 1], [1, 1, 1]),
        (list(range(0, 100, 2)), list(range(1, 101, 2))),
        ([-1000, -500, 0, 500, 1000], [42]),
    ],
)
def test_monotonicity_against_sorted_concat(a, b):
    # Cross-check against a simple sorted + direct median calculation
    merged = sorted(a + b)
    m = len(merged)
    if m % 2:
        expected = float(merged[m // 2])
    else:
        expected = (merged[m // 2 - 1] + merged[m // 2]) / 2.0
    assert median_two_sorted_merge(a, b) == pytest.approx(expected, rel=1e-12, abs=1e-12)
