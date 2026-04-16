from beautiful_dsa_algos_coding_interviews.queue.moving_average_from_data_stream import MovingAverage


def test_moving_average_stream():
    moving_average = MovingAverage(3)
    assert moving_average.next(1) == 1.0
    assert moving_average.next(10) == 5.5
    assert moving_average.next(3) == 14 / 3
    assert moving_average.next(5) == 6.0
