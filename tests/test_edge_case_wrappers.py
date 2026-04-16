from beautiful_dsa_algos_coding_interviews.backtracking.edge_cases import (
    combination_sum_with_edge_cases,
    combination_sum_ii_with_edge_cases,
    compute_permutations_with_edge_cases,
    generate_parentheses_with_edge_cases,
    letter_combinations_with_edge_cases,
    palindrome_partitioning_with_edge_cases,
    solve_n_queens_with_edge_cases,
    subsets_fixed_with_edge_cases,
    word_search_with_edge_cases,
)
from beautiful_dsa_algos_coding_interviews.graphs.edge_cases import (
    can_finish_dfs_with_edge_cases,
    can_finish_kahn_with_edge_cases,
    connected_components_with_edge_cases,
    unique_paths_with_obstacles_edge_cases,
)
from beautiful_dsa_algos_coding_interviews.intervals.edge_cases import (
    can_attend_meetings_with_edge_cases,
    merge_overlapping_intervals_with_edge_cases,
    min_meeting_rooms_with_edge_cases,
)
from beautiful_dsa_algos_coding_interviews.math.edge_cases import (
    get_antidiagonals_with_edge_cases,
    rotate_image_with_edge_cases,
)
from beautiful_dsa_algos_coding_interviews.prefix.edge_cases import (
    product_except_self_with_edge_cases,
)
from beautiful_dsa_algos_coding_interviews.search.bfs.edge_cases import (
    ladder_length_with_edge_cases,
)
from beautiful_dsa_algos_coding_interviews.sliding_window.edge_cases import (
    length_of_longest_substring_with_edge_cases,
    longest_ones_with_edge_cases,
)
from beautiful_dsa_algos_coding_interviews.stack.edge_cases import (
    is_valid_parentheses_with_edge_cases,
)
from beautiful_dsa_algos_coding_interviews.strings.edge_cases import (
    generate_anagrams_with_edge_cases,
    longest_palindrome_with_edge_cases,
)
from beautiful_dsa_algos_coding_interviews.trees.binary_tree.edge_cases import (
    max_depth_postorder_with_edge_cases,
    rightmost_node_binary_tree_with_edge_cases,
    tree_paths_with_edge_cases,
)
from beautiful_dsa_algos_coding_interviews.trees.binary_tree.tree_node import TreeNode
from beautiful_dsa_algos_coding_interviews.two_pointers.edge_cases import (
    is_palindrome_with_edge_cases,
    three_sum_bf_with_edge_cases,
    three_sum_with_edge_cases,
)


def test_backtracking_edge_case_wrappers():
    assert combination_sum_with_edge_cases([], 4) == []
    assert combination_sum_with_edge_cases([1, 2], 0) == [[]]
    assert combination_sum_ii_with_edge_cases([], 4) == []
    assert letter_combinations_with_edge_cases("10") == []
    assert compute_permutations_with_edge_cases([]) == [[]]
    assert subsets_fixed_with_edge_cases([]) == [[]]
    assert generate_parentheses_with_edge_cases(-1) == []
    assert solve_n_queens_with_edge_cases(0) == []
    assert palindrome_partitioning_with_edge_cases(None) == []
    assert word_search_with_edge_cases(None, "A") is False


def test_graph_edge_case_wrappers():
    assert can_finish_kahn_with_edge_cases(1, []) is True
    assert can_finish_dfs_with_edge_cases(0, []) is True
    assert connected_components_with_edge_cases([]) == 0
    assert unique_paths_with_obstacles_edge_cases([]) == 0


def test_interval_edge_case_wrappers():
    assert can_attend_meetings_with_edge_cases([]) is True
    assert merge_overlapping_intervals_with_edge_cases([[1, 3]]) == [[1, 3]]
    assert min_meeting_rooms_with_edge_cases([]) == 0


def test_math_and_prefix_edge_case_wrappers():
    assert get_antidiagonals_with_edge_cases([]) == []
    matrix = [[1]]
    assert rotate_image_with_edge_cases(matrix) == [[1]]
    assert product_except_self_with_edge_cases([5]) == [1]


def test_search_sliding_stack_string_edge_case_wrappers():
    assert ladder_length_with_edge_cases("hit", "hit", ["hit"]) == 1
    assert length_of_longest_substring_with_edge_cases("") == 0
    assert longest_ones_with_edge_cases([], 2) == 0
    assert is_valid_parentheses_with_edge_cases("") is True
    assert generate_anagrams_with_edge_cases(None) == []
    assert longest_palindrome_with_edge_cases(None) == ""


def test_two_pointer_edge_case_wrappers():
    assert is_palindrome_with_edge_cases(None) is False
    assert three_sum_with_edge_cases([1, 2]) == []
    assert three_sum_bf_with_edge_cases([1, 2]) == []


def test_tree_edge_case_wrappers():
    assert tree_paths_with_edge_cases(None) == []
    assert rightmost_node_binary_tree_with_edge_cases(None) == []
    assert max_depth_postorder_with_edge_cases(None) == 0

    root = TreeNode(1)
    root.right = TreeNode(2)
    assert rightmost_node_binary_tree_with_edge_cases(root) == [1, 2]
