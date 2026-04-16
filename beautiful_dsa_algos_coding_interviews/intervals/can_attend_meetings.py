from typing import List


def can_attend_meetings(intervals: List[List[int]]) -> bool:
    """
    Return True when no meeting overlaps with the next one after sorting by start.

    Time complexity: O(N log N) for sorting.
    Space complexity: O(N) if the sort allocates a new list.
    """

    if len(intervals) < 2:
        return True

    sorted_intervals = sorted(intervals, key=lambda interval: interval[0])
    for index in range(1, len(sorted_intervals)):
        previous_end = sorted_intervals[index - 1][1]
        current_start = sorted_intervals[index][0]
        if current_start < previous_end:
            return False
    return True
