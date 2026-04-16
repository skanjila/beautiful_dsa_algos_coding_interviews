from typing import List

from beautiful_dsa_algos_coding_interviews.backtracking.combination_sum import combination_sum
from beautiful_dsa_algos_coding_interviews.backtracking.combination_sum_ii import (
    combination_sum_ii,
)
from beautiful_dsa_algos_coding_interviews.backtracking.generate_parentheses import (
    generate_parentheses,
)
from beautiful_dsa_algos_coding_interviews.backtracking.letter_combinations_of_phone_number import (
    letter_combinations,
)
from beautiful_dsa_algos_coding_interviews.backtracking.n_queens import solve_n_queens
from beautiful_dsa_algos_coding_interviews.backtracking.palindrome_partitioning import (
    palindrome_partitioning,
)
from beautiful_dsa_algos_coding_interviews.backtracking.permutations import (
    compute_permutations,
)
from beautiful_dsa_algos_coding_interviews.backtracking.subsets import subsets_fixed
from beautiful_dsa_algos_coding_interviews.backtracking.word_search import word_search


def combination_sum_with_edge_cases(candidates: List[int], target: int) -> List[List[int]]:
    """Guard wrapper for ``combination_sum``.

    Time complexity: Same asymptotic complexity as ``combination_sum`` after
    constant-time edge checks.
    Space complexity: Same as the wrapped function.
    """
    if target < 0:
        return []
    if target == 0:
        return [[]]
    if not candidates:
        return []
    return combination_sum(candidates, target)


def combination_sum_ii_with_edge_cases(candidates: List[int], target: int) -> List[List[int]]:
    """Guard wrapper for ``combination_sum_ii``.

    Time complexity: Same asymptotic complexity as ``combination_sum_ii`` after
    constant-time edge checks.
    Space complexity: Same as the wrapped function.
    """
    if target < 0:
        return []
    if target == 0:
        return [[]]
    if not candidates:
        return []
    return combination_sum_ii(candidates, target)


def letter_combinations_with_edge_cases(digits: str) -> List[str]:
    """Guard wrapper for ``letter_combinations``.

    Time complexity: O(4^N) in the worst case after linear validation.
    Space complexity: Same as the wrapped function.
    """
    if not digits:
        return []
    if any(digit not in {"2", "3", "4", "5", "6", "7", "8", "9"} for digit in digits):
        return []
    return letter_combinations(digits)


def compute_permutations_with_edge_cases(nums: List[int]) -> List[List[int]]:
    """Guard wrapper for ``compute_permutations``.

    Time complexity: O(N * N!) for non-null input.
    Space complexity: Same as the wrapped function.
    """
    if nums is None:
        return []
    return compute_permutations(nums)


def subsets_fixed_with_edge_cases(nums: List[int]) -> List[List[int]]:
    """Guard wrapper for ``subsets_fixed``.

    Time complexity: O(N * 2^N) for non-null input.
    Space complexity: Same as the wrapped function.
    """
    if nums is None:
        return []
    if not nums:
        return [[]]
    return subsets_fixed(nums)


def generate_parentheses_with_edge_cases(n: int) -> List[str]:
    """Guard wrapper for ``generate_parentheses``.

    Time complexity: O(C_n * n) for valid input.
    Space complexity: Same as the wrapped function.
    """
    if n < 0:
        return []
    return generate_parentheses(n)


def solve_n_queens_with_edge_cases(n: int) -> List[List[str]]:
    """Guard wrapper for ``solve_n_queens``.

    Time complexity: O(N!) in the worst case.
    Space complexity: Same as the wrapped function.
    """
    if n <= 0:
        return []
    return solve_n_queens(n)


def palindrome_partitioning_with_edge_cases(s: str) -> List[List[str]]:
    """Guard wrapper for ``palindrome_partitioning``.

    Time complexity: O(N * 2^N) for non-null input.
    Space complexity: Same as the wrapped function.
    """
    if s is None:
        return []
    return palindrome_partitioning(s)


def word_search_with_edge_cases(board: List[List[str]], word: str) -> bool:
    """Guard wrapper for ``word_search``.

    Time complexity: O(R * C * 4^L) for non-null input.
    Space complexity: Same as the wrapped function.
    """
    if board is None:
        return False
    return word_search(board, word)
