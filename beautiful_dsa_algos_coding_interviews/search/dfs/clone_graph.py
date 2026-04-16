from __future__ import annotations

from typing import Dict, List, Optional


class GraphNode:
    """
    Undirected graph node for graph-cloning problems.

    Time complexity: O(1) to construct.
    Space complexity: O(1) per node, excluding neighbors.
    """

    def __init__(self, val: int = 0, neighbors: Optional[List["GraphNode"]] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Optional[GraphNode]) -> Optional[GraphNode]:
    """
    Deep-copy a connected graph using DFS and a visited map.

    Time complexity: O(V + E)
    Space complexity: O(V) for the clone map and recursion stack.
    """

    if node is None:
        return None

    clones: Dict[GraphNode, GraphNode] = {}

    def dfs(current: GraphNode) -> GraphNode:
        if current in clones:
            # Reuse the existing clone to break cycles and shared-neighbor repeats.
            return clones[current]

        copied = GraphNode(current.val)
        clones[current] = copied

        for neighbor in current.neighbors:
            # Clone neighbors recursively, then attach them to the copied node.
            copied.neighbors.append(dfs(neighbor))

        return copied

    return dfs(node)
