from beautiful_dsa_algos_coding_interviews.linked_list.list_node import ListNode
from beautiful_dsa_algos_coding_interviews.linked_list.merge_two_sorted_lists import (
    merge_two_sorted_lists,
)
from beautiful_dsa_algos_coding_interviews.linked_list.reverse_linked_list import (
    reverse_linked_list,
)


def build_list(values):
    dummy = ListNode()
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


def to_list(head):
    result = []
    while head is not None:
        result.append(head.val)
        head = head.next
    return result


def test_reverse_linked_list():
    assert to_list(reverse_linked_list(build_list([1, 2, 3]))) == [3, 2, 1]


def test_merge_two_sorted_lists():
    merged = merge_two_sorted_lists(build_list([1, 2, 4]), build_list([1, 3, 4]))
    assert to_list(merged) == [1, 1, 2, 3, 4, 4]
