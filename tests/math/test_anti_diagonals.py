import pytest

from beautiful_dsa_algos_coding_interviews.math.matrix_antidiagonals import get_antidiagonals


def test_square_matrix_3x3():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    expected = [
        [1],
        [2, 4],
        [3, 5, 7],
        [6, 8],
        [9]
    ]
    assert get_antidiagonals(matrix) == expected


def test_rectangular_matrix_2x3():
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    expected = [
        [1],
        [2, 4],
        [3, 5],
        [6]
    ]
    assert get_antidiagonals(matrix) == expected


def test_rectangular_matrix_3x2():
    matrix = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]
    expected = [
        [1],
        [2, 3],
        [4, 5],
        [6]
    ]
    assert get_antidiagonals(matrix) == expected


def test_single_row():
    matrix = [[10, 20, 30, 40]]
    expected = [
        [10],
        [20],
        [30],
        [40]
    ]
    assert get_antidiagonals(matrix) == expected


def test_single_column():
    matrix = [
        [1],
        [2],
        [3],
        [4]
    ]
    expected = [
        [1],
        [2],
        [3],
        [4]
    ]
    assert get_antidiagonals(matrix) == expected


def test_one_element():
    matrix = [[42]]
    expected = [[42]]
    assert get_antidiagonals(matrix) == expected


def test_non_square_large():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8]
    ]
    expected = [
        [1],
        [2, 5],
        [3, 6],
        [4, 7],
        [8]
    ]
    assert get_antidiagonals(matrix) == expected


def test_empty_matrix_raises():
    with pytest.raises(IndexError):
        get_antidiagonals([])
