import heapq
from typing import List


def min_meeting_rooms(intervals: List[List[int]]) -> int:
    """
    Return the minimum number of concurrent meeting rooms required.

    Time complexity: O(N log N) because sorting dominates and each heap
    operation costs O(log N).
    Space complexity: O(N) for the heap in the worst case.
    """

    if not intervals:
        return 0

    sorted_intervals = sorted(intervals, key=lambda interval: interval[0])
    active_meetings: List[int] = []

    for start, end in sorted_intervals:
        while active_meetings and active_meetings[0] <= start:
            heapq.heappop(active_meetings)
        heapq.heappush(active_meetings, end)

    return len(active_meetings)
