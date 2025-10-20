from typing import List

"""
Step-by-step idea:

We are given an adjacency matrix `isConnected`, where:
    isConnected[i][j] == 1 means there is a connection (an edge) between node i and node j
    isConnected[i][j] == 0 means there is no connection.

Goal:
We want to count how many *connected components* exist in this undirected graph.
A connected component is a set of nodes that are all reachable from one another.

Strategy:
1. Keep track of which nodes you’ve visited.
   -> This prevents counting the same node multiple times.

2. Loop through all nodes (from 0 to n-1).
   -> Each time you find a node that hasn’t been visited yet,
      that means you’ve discovered a *new* connected component.

3. From that node, perform a DFS (Depth-First Search)
   -> This explores all nodes reachable from that starting node.
   -> Mark all those nodes as visited (they belong to the same component).

4. Continue looping.
   -> Each time you find another unvisited node, that’s another new component.

5. Return the total number of connected components at the end.
"""

def findConnectedComponents(isConnected: List[List[int]]) -> int:
    # Number of nodes (cities / vertices)
    visited_length = len(isConnected)

    # Track which nodes have been visited during DFS.
    # Initially, no node is visited.
    visited = [False] * visited_length

    # Counter for how many connected components we've found so far.
    connected_components = 0

    # Iterate through all nodes (0, 1, 2, ..., n-1)
    for i in range(visited_length):
        # If this node has NOT been visited yet,
        # it must be part of a *new* connected component.
        if not visited[i]:
            connected_components += 1  # Found a new component
            dfs_helper(i, visited, isConnected)  # Explore all reachable nodes from i

    # After visiting all nodes, return how many components we found.
    return connected_components


def dfs_helper(start_index: int, visited: List[bool], isConnected: List[List[int]]) -> None:
    """
    Recursive helper function to perform a depth-first search (DFS)
    starting from the node `start_index`.

    Marks all nodes reachable from `start_index` as visited.
    """
    # Mark this node as visited so we don’t revisit it again.
    visited[start_index] = True

    # Get the total number of nodes.
    n = len(isConnected)

    # Explore all possible neighbors of the current node.
    for j in range(n):
        # If there is an edge between start_index and j (isConnected[start_index][j] == 1)
        # AND we haven't visited node j yet,
        # then recursively visit node j.
        if isConnected[start_index][j] == 1 and not visited[j]:
            dfs_helper(j, visited, isConnected)  # Recurse deeper into the graph
