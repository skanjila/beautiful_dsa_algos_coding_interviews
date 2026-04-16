import pytest

from beautiful_dsa_algos_coding_interviews.binary_search.median_of_two_sorted_arrays import (
    median_two_sorted_merge,
)
from beautiful_dsa_algos_coding_interviews.binary_search.median_of_two_sorted_arrays_edge_cases import (
    median_two_sorted_with_edge_cases,
)


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ([1], [], 1.0),
        ([], [2], 2.0),
        ([-7, -3, -1], [-5, -4, -2], -3.5),
        ([1, 2, 3, 4, 5], [6], 3.5),
        ([10, 20, 30], [10, 20, 30], 20.0),
    ],
)
def test_median_edge_cases(a, b, expected):
    assert median_two_sorted_merge(a, b) == pytest.approx(expected, rel=1e-12, abs=1e-12)
    assert median_two_sorted_with_edge_cases(a, b) == pytest.approx(
        expected, rel=1e-12, abs=1e-12
    )


def test_median_edge_case_raises_on_both_empty():
    with pytest.raises(ValueError):
        median_two_sorted_with_edge_cases([], [])
