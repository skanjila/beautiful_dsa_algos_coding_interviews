from collections import deque
from typing import List


def find_order(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
    """
    Return one valid topological ordering of courses, or [] if impossible.

    Time complexity: O(V + E) because adjacency construction and Kahn's
    traversal each process every vertex and edge a constant number of times.
    Space complexity: O(V + E) for the graph, indegrees, and queue.
    """
    graph = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1

    queue = deque(course for course in range(num_courses) if indegree[course] == 0)
    order: List[int] = []

    while queue:
        course = queue.popleft()
        order.append(course)

        for next_course in graph[course]:
            indegree[next_course] -= 1
            if indegree[next_course] == 0:
                queue.append(next_course)

    return order if len(order) == num_courses else []
