from typing import Optional

from beautiful_dsa_algos_coding_interviews.linked_list.list_node import ListNode


def reverse_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse a singly linked list iteratively.

    Time complexity: O(N)
    Space complexity: O(1)
    """

    prev = None
    current = head

    while current is not None:
        # Save the rest of the list before we reverse the current pointer.
        nxt = current.next
        current.next = prev
        # Slide the two-pointer window forward by one node.
        prev = current
        current = nxt

    return prev
