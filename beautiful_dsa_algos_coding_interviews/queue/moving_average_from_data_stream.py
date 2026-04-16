from collections import deque


class MovingAverage:
    """
    Fixed-size moving average over a stream.

    Time complexity: O(1) per next call because each value is appended once and
    evicted at most once.
    Space complexity: O(size) because the queue stores only the active window.
    """

    def __init__(self, size: int):
        if size <= 0:
            raise ValueError("size must be positive")
        self.size = size
        self.queue = deque()
        self.running_sum = 0.0

    def next(self, value: int) -> float:
        self.queue.append(value)
        self.running_sum += value

        if len(self.queue) > self.size:
            self.running_sum -= self.queue.popleft()

        return self.running_sum / len(self.queue)
