import itertools
import pytest

from beautiful_dsa_algos_coding_interviews.backtracking.letter_combinations_of_phone_number import \
    letter_combinations

KEYPAD = {
    "2": "abc", "3": "def",
    "4": "ghi", "5": "jkl", "6": "mno",
    "7": "pqrs", "8": "tuv", "9": "wxyz",
}


def expected_bruteforce(digits: str):
    """Reference generator using itertools.product for cross-checking."""
    if not digits:
        return []
    pools = [KEYPAD[d] for d in digits]
    return ["".join(t) for t in itertools.product(*pools)]


def product_count(digits: str) -> int:
    """Number of combinations = product of letter counts per digit."""
    if not digits:
        return 0
    prod = 1
    for d in digits:
        prod *= len(KEYPAD[d])
    return prod


def test_empty_input_returns_empty_list():
    assert letter_combinations("") == []


@pytest.mark.parametrize(
    "digit, expected",
    [
        ("2", {"a", "b", "c"}),
        ("7", {"p", "q", "r", "s"}),  # 4-letter key
    ],
)
def test_single_digit_all_letters_returned(digit, expected):
    result = set(letter_combinations(digit))
    assert result == expected


def test_two_digits_matches_known_set_for_23():
    # Order is unspecified, so compare sets
    expected = {"ad","ae","af","bd","be","bf","cd","ce","cf"}
    assert set(letter_combinations("23")) == expected


@pytest.mark.parametrize(
    "digits",
    [
        "23",
        "79",      # 4 * 4 = 16
        "278",     # 3 * 4 * 3 = 36
        "946",     # 4 * 3 * 3 = 36
    ],
)
def test_size_matches_product_of_letter_counts(digits):
    result = letter_combinations(digits)
    assert len(result) == product_count(digits)


@pytest.mark.parametrize("digits", ["23", "79", "546", "888"])
def test_all_combinations_use_only_valid_letters(digits):
    result = letter_combinations(digits)
    valid_sets = [set(KEYPAD[d]) for d in digits]
    for combo in result:
        assert len(combo) == len(digits)
        for ch, valid in zip(combo, valid_sets):
            assert ch in valid


@pytest.mark.parametrize("digits", ["236", "94", "772"])
def test_results_match_itertools_reference(digits):
    # Strong cross-check against a brute-force construction
    assert set(letter_combinations(digits)) == set(expected_bruteforce(digits))
