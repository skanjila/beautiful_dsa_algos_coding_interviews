from beautiful_dsa_algos_coding_interviews.search.dfs.max_area_of_island import (
    max_area_of_island,
)


def test_max_area_of_island():
    grid = [
        [0, 0, 1, 0, 0],
        [1, 1, 1, 0, 1],
        [0, 1, 0, 0, 1],
        [0, 0, 0, 1, 1],
    ]
    assert max_area_of_island(grid) == 5
