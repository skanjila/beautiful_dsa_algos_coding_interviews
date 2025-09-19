
def is_valid_parentheses(s: str) -> bool:
    """
    Validate parentheses using a stack.
    Time: O(n), Space: O(n)
    """
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for char in s:
        if char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
    return not stack
