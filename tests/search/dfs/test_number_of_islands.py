from beautiful_dsa_algos_coding_interviews.search.dfs.number_of_islands import (
    number_of_islands,
)


def test_number_of_islands_basic():
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert number_of_islands(grid) == 3


def test_number_of_islands_empty():
    assert number_of_islands([]) == 0
