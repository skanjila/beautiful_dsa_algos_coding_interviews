from typing import List

from beautiful_dsa_algos_coding_interviews.intervals.can_attend_meetings import (
    can_attend_meetings,
)
from beautiful_dsa_algos_coding_interviews.intervals.merge_overlapping_intervals import (
    merge_overlapping_intervals,
)
from beautiful_dsa_algos_coding_interviews.intervals.min_meeting_rooms import (
    min_meeting_rooms,
)


def can_attend_meetings_with_edge_cases(intervals: List[List[int]]) -> bool:
    """Guard wrapper for ``can_attend_meetings``.

    Time complexity: O(N log N) in the general case.
    Space complexity: Same as the wrapped function.
    """
    if len(intervals) < 2:
        return True
    return can_attend_meetings(intervals)


def merge_overlapping_intervals_with_edge_cases(intervals: List[List[int]]) -> List[List[int]]:
    """Guard wrapper for interval merging.

    Time complexity: O(N log N) in the general case.
    Space complexity: Same as the wrapped function.
    """
    if not intervals:
        return []
    if len(intervals) == 1:
        return [intervals[0][:]]
    return merge_overlapping_intervals(intervals)


def min_meeting_rooms_with_edge_cases(intervals: List[List[int]]) -> int:
    """Guard wrapper for meeting-room counting.

    Time complexity: O(N log N) in the general case.
    Space complexity: Same as the wrapped function.
    """
    if not intervals:
        return 0
    if len(intervals) == 1:
        return 1
    return min_meeting_rooms(intervals)
