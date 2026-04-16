from beautiful_dsa_algos_coding_interviews.stack.simplify_path import simplify_path


def test_simplify_path_basic():
    assert simplify_path("/home/") == "/home"


def test_simplify_path_parent_segments():
    assert simplify_path("/a/./b/../../c/") == "/c"
