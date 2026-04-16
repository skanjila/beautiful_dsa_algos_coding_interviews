from beautiful_dsa_algos_coding_interviews.stack.match_parenthesees import (
    is_valid_parentheses,
)


def is_valid_parentheses_with_edge_cases(s: str) -> bool:
    """Guard wrapper for ``is_valid_parentheses``.

    Time complexity: O(N) for non-null strings.
    Space complexity: Same as the wrapped function.
    """
    if s == "":
        return True
    if s is None:
        return False
    return is_valid_parentheses(s)
