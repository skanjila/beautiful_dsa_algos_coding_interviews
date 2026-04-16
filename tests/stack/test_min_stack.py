from beautiful_dsa_algos_coding_interviews.stack.min_stack import MinStack


def test_min_stack_tracks_minimum():
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    assert stack.get_min() == -3
    stack.pop()
    assert stack.top() == 0
    assert stack.get_min() == -2
