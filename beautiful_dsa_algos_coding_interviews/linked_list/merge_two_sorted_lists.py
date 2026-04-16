from typing import Optional

from beautiful_dsa_algos_coding_interviews.linked_list.list_node import ListNode


def merge_two_sorted_lists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    """
    Merge two sorted linked lists into one sorted list.

    Time complexity: O(M + N)
    Space complexity: O(1) auxiliary
    """

    dummy = ListNode()
    tail = dummy

    while list1 is not None and list2 is not None:
        # Attach the smaller head node, because that node is guaranteed to be
        # next in the merged sorted order.
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    # One list may still have leftover nodes; they are already sorted.
    tail.next = list1 if list1 is not None else list2
    return dummy.next
