from typing import List


def decode_string(text: str) -> str:
    """
    Decode bracketed repeat expressions like '3[a2[c]]'.

    Time complexity: O(N * K) in the common analysis because the parser scans
    the input once, but repeated substring materialization contributes to the
    final output size K.
    Space complexity: O(N + K) for the stack state plus the decoded output.
    """
    counts: List[int] = []
    fragments: List[str] = []
    current = ""
    number = 0

    for char in text:
        if char.isdigit():
            number = number * 10 + int(char)
        elif char == "[":
            counts.append(number)
            fragments.append(current)
            number = 0
            current = ""
        elif char == "]":
            repeat = counts.pop()
            prefix = fragments.pop()
            current = prefix + current * repeat
        else:
            current += char

    return current
