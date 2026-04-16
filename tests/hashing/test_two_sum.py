import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from beautiful_dsa_algos_coding_interviews.hashing.two_sum import two_sum
from beautiful_dsa_algos_coding_interviews.hashing.edge_cases import (
    two_sum_with_edge_cases,
)


def test_two_sum_basic_case():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]


def test_two_sum_with_duplicates():
    assert two_sum([3, 3], 6) == [0, 1]


def test_two_sum_with_negative_numbers():
    assert two_sum([-3, 4, 3, 90], 0) == [0, 2]


def test_two_sum_no_solution():
    assert two_sum([1, 2, 3], 10) == []


def test_two_sum_edge_case_wrapper():
    assert two_sum_with_edge_cases(None, 5) == []
    assert two_sum_with_edge_cases([1], 1) == []
    assert two_sum_with_edge_cases([2, 7, 11, 15], 9) == [0, 1]
