# Intervals Deep Dive

Interval problems almost always begin with sorting by start time.

## Interview Approach

When you hear "interval", ask:

- do I need to detect overlap?
- do I need to merge ranges?
- do I need the number of simultaneous active intervals?

Fast pattern map:

- overlap detection -> sort and compare neighbors
- merging -> sort and maintain one active interval
- concurrency count -> sort plus min-heap of end times

## `can_attend_meetings`

Checks whether any meeting overlaps with the next after sorting.

- If `current_start < previous_end`, the schedule conflicts.
- Pattern to use quickly: sorted neighbor comparison.
- Big O: `O(N log N)` time because sorting the intervals is the expensive step;
  the overlap check afterward is just one linear pass. Space is often described
  as `O(N)` here because sorting may allocate additional memory depending on the
  runtime and because the implementation works on a copied/ordered list.

## `merge_overlapping_intervals`

Merges contiguous or overlapping intervals into maximal ranges.

- Keep one active merged interval.
- Extend it when the next interval overlaps; otherwise start a new merged block.
- Pattern to use quickly: sort + rolling merge.
- Big O: `O(N log N)` time because you first sort by start time and then merge
  intervals in one left-to-right pass. Space is `O(N)` because the merged
  output can contain up to all intervals in the no-overlap case.

## `min_meeting_rooms`

Counts how many concurrent meeting end times are active.

- Sort by start time.
- Min-heap tracks the earliest ending active meeting.
- Pop finished meetings before adding the next one.
- Pattern to use quickly: sweep line / heap of active interval end times.
- Big O: `O(N log N)` time because sorting meetings by start time costs
  `N log N`, and each meeting then triggers a heap push/pop of `log N`.
  Space is `O(N)` in the worst case when many meetings overlap at once.

## `edge_cases`

Wrappers explicitly handle empty schedules and one-interval inputs. The general
algorithmic cost is unchanged.
