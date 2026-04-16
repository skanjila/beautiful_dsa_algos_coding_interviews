def string_to_integer(text: str) -> int:
    """
    Parse an integer with optional whitespace and sign, clamped to 32-bit range.

    Time complexity: O(N) because the parser walks the string from left to right
    once until the numeric run ends.
    Space complexity: O(1) because only scalar parser state is maintained.
    """
    index = 0
    length = len(text)

    while index < length and text[index] == " ":
        index += 1

    sign = 1
    if index < length and text[index] in "+-":
        sign = -1 if text[index] == "-" else 1
        index += 1

    value = 0
    while index < length and text[index].isdigit():
        value = value * 10 + int(text[index])
        index += 1

    value *= sign
    lower_bound = -(2**31)
    upper_bound = 2**31 - 1
    if value < lower_bound:
        return lower_bound
    if value > upper_bound:
        return upper_bound
    return value
