# tests/graphs/test_find_circle_num.py
import pytest

from beautiful_dsa_algos_coding_interviews.graphs.connected_components import findConnectedComponents


@pytest.mark.parametrize(
    "matrix, expected",
    [
        # --- Edge cases ---
        ([], 0),                                # empty graph
        ([[1]], 1),                             # single node

        # --- Simple cases ---
        ([[1, 0],
          [0, 1]], 2),                          # two isolated nodes

        ([[1, 1],
          [1, 1]], 1),                          # two nodes connected

        # --- Chain (still one province) ---
        ([[1, 1, 0],
          [1, 1, 1],
          [0, 1, 1]], 1),

        # --- Three components (block diagonal) ---
        ([[1, 1, 0, 0, 0],
          [1, 1, 0, 0, 0],
          [0, 0, 1, 0, 0],
          [0, 0, 0, 1, 1],
          [0, 0, 0, 1, 1]], 3),

        # --- Diagonal zeros (non-standard input): treated as isolated unless connected via off-diagonal 1s
        ([[0, 0],
          [0, 0]], 2),

        # --- Asymmetric input (non-standard): DFS still follows out-edges from each i
        # Here: 0->1 but 1!->0; still one traversal from node 0 reaches 1
        ([[1, 1, 0],
          [0, 1, 0],
          [0, 0, 1]], 2),  # nodes {0,1} connected by out-edge; node 2 isolated
    ],
)
def test_find_circle_num_parametrized(matrix, expected):
    # function signature includes `self`, so pass None
    assert findConnectedComponents(matrix) == expected


def test_large_two_block_components():
    """
    Build a block-diagonal adjacency matrix:
      - Block A: 100 nodes, fully connected
      - Block B: 200 nodes, fully connected
      - No edges between blocks
    Expect 2 connected components.
    """
    a, b = 100, 200
    n = a + b

    # Start with zeros
    mat = [[0] * n for _ in range(n)]

    # Fully connect block A
    for i in range(a):
        for j in range(a):
            mat[i][j] = 1

    # Fully connect block B
    for i in range(a, n):
        for j in range(a, n):
            mat[i][j] = 1

    assert findConnectedComponents(mat) == 2


def test_single_island_inside_sparse_graph():
    """
    Mostly zeros with a tiny 3-node island connected together.
    Expect: isolated nodes + one island.
    n = 8; island = {2,3,5} fully connected among themselves.
    Components: {0}, {1}, {2,3,5}, {4}, {6}, {7} => 6
    """
    n = 8
    mat = [[0] * n for _ in range(n)]
    # diagonals often 1 in LeetCode, but we keep zeros to prove robustness
    island = [2, 3, 5]
    for i in island:
        for j in island:
            if i == j:
                mat[i][j] = 1
            else:
                mat[i][j] = 1
    # leave others as zeros (isolated)
    assert findConnectedComponents(mat) == 6
