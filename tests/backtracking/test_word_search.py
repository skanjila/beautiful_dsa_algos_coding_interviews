from beautiful_dsa_algos_coding_interviews.backtracking.word_search import word_search


def test_word_search_found():
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]
    assert word_search(board, "ABCCED") is True


def test_word_search_missing():
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]
    assert word_search(board, "ABCB") is False


def test_word_search_empty_word():
    assert word_search([["A"]], "") is True
