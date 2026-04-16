class MinStack:
    """
    Stack that returns the current minimum in O(1) time.

    Time complexity: O(1) for push, pop, top, and get_min because each method
    touches only the last entry of one or two internal stacks.
    Space complexity: O(N) because every pushed value may also contribute to the
    min stack.
    """

    def __init__(self) -> None:
        self.stack = []
        self.min_stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self) -> None:
        value = self.stack.pop()
        if value == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def get_min(self) -> int:
        return self.min_stack[-1]
