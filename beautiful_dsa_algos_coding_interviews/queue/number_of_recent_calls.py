from collections import deque


class RecentCounter:
    """
    Count requests that happened in the last 3000 milliseconds.

    Time complexity: O(1) amortized per ping because each timestamp enters the
    queue once and leaves once.
    Space complexity: O(W) where W is the number of timestamps in the active
    3000ms window.
    """

    def __init__(self):
        self.queue = deque()

    def ping(self, timestamp: int) -> int:
        self.queue.append(timestamp)
        lower_bound = timestamp - 3000

        while self.queue and self.queue[0] < lower_bound:
            self.queue.popleft()

        return len(self.queue)
