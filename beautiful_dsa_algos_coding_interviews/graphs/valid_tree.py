from typing import List


def valid_tree(n: int, edges: List[List[int]]) -> bool:
    """
    Check whether an undirected graph forms one valid tree.

    Time complexity: O(V + E) because adjacency construction is linear and DFS
    visits each node and edge a constant number of times.
    Space complexity: O(V + E) for the graph plus visited set and recursion stack.
    """
    if len(edges) != n - 1:
        # A tree with n nodes must have exactly n - 1 edges.
        return False

    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited = set()

    def dfs(node: int, parent: int) -> None:
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            if neighbor not in visited:
                dfs(neighbor, node)

    dfs(0, -1)
    return len(visited) == n
