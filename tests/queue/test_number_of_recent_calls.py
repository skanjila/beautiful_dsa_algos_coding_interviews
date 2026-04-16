from beautiful_dsa_algos_coding_interviews.queue.number_of_recent_calls import RecentCounter


def test_recent_counter_window():
    counter = RecentCounter()
    assert counter.ping(1) == 1
    assert counter.ping(100) == 2
    assert counter.ping(3001) == 3
    assert counter.ping(3002) == 3
