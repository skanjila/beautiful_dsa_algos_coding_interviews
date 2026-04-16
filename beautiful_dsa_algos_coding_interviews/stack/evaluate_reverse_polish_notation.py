from typing import List


def eval_rpn(tokens: List[str]) -> int:
    """
    Evaluate a reverse Polish notation expression.

    Time complexity: O(N) because each token is processed once.
    Space complexity: O(N) in the worst case for the operand stack.
    """
    stack: List[int] = []

    for token in tokens:
        if token in {"+", "-", "*", "/"}:
            right = stack.pop()
            left = stack.pop()

            if token == "+":
                stack.append(left + right)
            elif token == "-":
                stack.append(left - right)
            elif token == "*":
                stack.append(left * right)
            else:
                # Truncate toward zero to match the usual interview definition.
                stack.append(int(left / right))
        else:
            stack.append(int(token))

    return stack[-1]
