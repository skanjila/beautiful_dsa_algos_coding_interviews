from collections import deque
from typing import List


def is_bipartite(graph: List[List[int]]) -> bool:
    """
    Check whether an undirected graph can be 2-colored.

    Time complexity: O(V + E) because each node is colored once and each edge is
    inspected from its incident adjacency lists.
    Space complexity: O(V) for the color map and BFS queue.
    """
    color = {}

    for start in range(len(graph)):
        if start in color:
            continue

        queue = deque([start])
        color[start] = 0

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in color:
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False

    return True
