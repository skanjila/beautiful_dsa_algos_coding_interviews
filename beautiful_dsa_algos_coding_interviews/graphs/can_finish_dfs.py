from collections import defaultdict
from typing import List

def can_finish_dfs(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    Determines if it’s possible to finish all courses given a list of prerequisites.
    This is the DFS-based cycle detection approach for the "Course Schedule" problem (LeetCode 207).

    Parameters:
        numCourses: total number of courses (labeled from 0 to numCourses-1)
        prerequisites: list of [course, prereq] pairs meaning
                       "to take course, you must first complete prereq"

    Returns:
        True if you can finish all courses (no cycles in dependency graph),
        False if there’s a cycle (some courses depend on each other).
    """

    # Build adjacency list representation of the graph:
    # pre[course] = list of courses that must be taken before 'course'
    pre = defaultdict(list)
    for course, p in prerequisites:
        pre[course].append(p)

    # A 'taken' set tracks nodes currently being visited in the DFS path.
    # If we revisit a node already in this set, it means there’s a cycle.
    taken = set()

    def dfs(course: int) -> bool:
        """
        Perform DFS to check for cycles starting from 'course'.
        Returns True if this path has no cycles, False otherwise.
        """

        # Base case: if there are no prerequisites left for this course,
        # it's considered safe — no cycle from this path.
        if not pre[course]:
            return True

        # If the course is already in the recursion stack (taken),
        # we found a cycle: this course indirectly depends on itself.
        if course in taken:
            return False

        # Mark this course as being visited (part of the current DFS path)
        taken.add(course)

        # Visit all its prerequisites recursively
        for p in pre[course]:
            # If any prerequisite leads to a cycle, abort immediately
            if not dfs(p):
                return False

        # If we reach here, no cycles were found along this path.
        # We can safely "clear" its prerequisite list to mark it as resolved.
        pre[course] = []  # Memoization: avoids re-checking same subtree
        taken.remove(course)  # Optional but cleaner; prevents side effects in other DFS calls

        return True

    # Try to start a DFS from every course,
    # because the graph might be disconnected (multiple components).
    for course in range(numCourses):
        if not dfs(course):
            # If any DFS detects a cycle, return False
            return False

    # If all DFS traversals succeeded (no cycles), we can finish all courses.
    return True
