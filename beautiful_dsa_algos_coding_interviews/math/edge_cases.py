from typing import List

from beautiful_dsa_algos_coding_interviews.math.matrix_antidiagonals import (
    get_antidiagonals,
)
from beautiful_dsa_algos_coding_interviews.math.matrix_rotation import rotate_image


def get_antidiagonals_with_edge_cases(matrix: List[List[int]]) -> List[List[int]]:
    """Guard wrapper for ``get_antidiagonals``.

    Time complexity: O(R * C) for non-empty matrices.
    Space complexity: Same as the wrapped function.
    """
    if not matrix or not matrix[0]:
        return []
    return get_antidiagonals(matrix)


def rotate_image_with_edge_cases(matrix: List[List[int]]) -> List[List[int]]:
    """Guard wrapper for ``rotate_image``.

    Time complexity: O(N^2) for square matrices.
    Space complexity: O(1) auxiliary space.
    """
    if matrix == []:
        return matrix
    rotate_image(matrix)
    return matrix
