from beautiful_dsa_algos_coding_interviews.backtracking.n_queens import solve_n_queens


def test_n_queens_one():
    assert solve_n_queens(1) == [["Q"]]


def test_n_queens_two_has_no_solution():
    assert solve_n_queens(2) == []


def test_n_queens_four_has_two_solutions():
    result = solve_n_queens(4)
    assert len(result) == 2
    assert all(len(board) == 4 for board in result)
    assert all(row.count("Q") == 1 for board in result for row in board)
