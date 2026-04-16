from typing import List


def encode(strings: List[str]) -> str:
    """
    Encode a list of strings into one transport-safe string.

    Time complexity: O(total_chars) because each character is written once along
    with a short length prefix per string.
    Space complexity: O(total_chars) for the encoded output.
    """
    return "".join(f"{len(value)}#{value}" for value in strings)


def decode(encoded: str) -> List[str]:
    """
    Decode the transport-safe representation back into the original list.

    Time complexity: O(total_chars) because the parser advances through the
    encoded string once while slicing each payload exactly once.
    Space complexity: O(total_chars) for the decoded strings.
    """
    result: List[str] = []
    index = 0

    while index < len(encoded):
        separator = index
        while encoded[separator] != "#":
            separator += 1

        length = int(encoded[index:separator])
        start = separator + 1
        end = start + length
        result.append(encoded[start:end])
        index = end

    return result
