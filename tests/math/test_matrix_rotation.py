# tests/math/test_matrix_rotation_rotate_image.py
import copy
import pytest

from beautiful_dsa_algos_coding_interviews.math.matrix_rotation import rotate_image


@pytest.mark.parametrize(
    "matrix,expected",
    [
        ([[5]], [[5]]),
        (
            [[1, 2],
             [3, 4]],
            [[3, 1],
             [4, 2]],
        ),
        (
            [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]],
            [[7, 4, 1],
             [8, 5, 2],
             [9, 6, 3]],
        ),
        (
            [[ 1,  2,  3,  4],
             [ 5,  6,  7,  8],
             [ 9, 10, 11, 12],
             [13, 14, 15, 16]],
            [[13,  9, 5, 1],
             [14, 10, 6, 2],
             [15, 11, 7, 3],
             [16, 12, 8, 4]],
        ),
    ],
)
def test_rotate_image_correct_and_returns_none(matrix, expected):
    # capture row object identities to ensure true in-place mutation
    row_ids_before = [id(r) for r in matrix]

    result = rotate_image(matrix)

    assert result is None, "Function should return None (in-place operation)."
    assert matrix == expected, "Matrix not rotated correctly."

    # rows should be the same list objects (mutated, not replaced)
    row_ids_after = [id(r) for r in matrix]
    assert row_ids_before == row_ids_after, "Rows should be mutated in place, not replaced."


def test_rotate_image_four_times_restores_original():
    m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    original = copy.deepcopy(m)

    for _ in range(4):
        rotate_image(m)

    assert m == original, "Four 90° rotations should restore the original matrix."


@pytest.mark.parametrize(
    "bad_matrix",
    [
        # rectangular (non-square)
        [[1, 2, 3],
         [4, 5, 6]],
        # ragged rows
        [[1, 2, 3],
         [4, 5]],
    ],
)
def test_non_square_or_ragged_inputs_raise_value_error(bad_matrix):
    with pytest.raises(ValueError):
        rotate_image(bad_matrix)


def test_empty_matrix_is_noop_and_returns_none():
    # Treat empty as a no-op; adjust if your spec requires raising instead.
    m = []
    result = rotate_image(m)
    assert result is None
    assert m == []
