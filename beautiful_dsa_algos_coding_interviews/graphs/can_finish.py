from collections import deque
from typing import List

# Solution for the Course Schedule problem using Kahn's Algorithm (BFS-based Topological Sort).
def can_finish_kahn(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """Given a number of courses and prerequisites, check if there exists a cycle in the graph preventing
    an individual ro finish the courses
    @param numCourses: number of courses
    @param prerequisites: list of prerequisites
    @return: True if there is a cycle, False otherwise"""
    finished_courses = 0

    graph_of_finished_courses: List[List[int]] = [[] for _ in range(numCourses)]
    indegree_of_courses = [0] * numCourses

    for course, prereq in prerequisites:
        # Edge prereq -> course
        graph_of_finished_courses[prereq].append(course)
        indegree_of_courses[course] += 1

    queue_of_courses = deque([i for i in range(numCourses) if indegree_of_courses[i] == 0])

    while queue_of_courses:
        cur_course = queue_of_courses.popleft()
        finished_courses += 1

        for neighboring_course in graph_of_finished_courses[cur_course]:
            indegree_of_courses[neighboring_course] -= 1
            if indegree_of_courses[neighboring_course] == 0:
                queue_of_courses.append(neighboring_course)

    return finished_courses == numCourses

