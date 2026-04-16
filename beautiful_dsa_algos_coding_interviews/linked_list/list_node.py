from typing import Optional


class ListNode:
    """
    Singly linked-list node used by linked-list exercises.

    Time complexity: O(1) to construct.
    Space complexity: O(1) per node, excluding the rest of the list.
    """

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next
