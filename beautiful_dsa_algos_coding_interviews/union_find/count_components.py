from typing import List

from beautiful_dsa_algos_coding_interviews.union_find.union_find import UnionFind


def count_components(n: int, edges: List[List[int]]) -> int:
    """
    Count connected components in an undirected graph using union-find.

    Time complexity: O((N + E) * alpha(N))
    Space complexity: O(N)
    """

    uf = UnionFind(n)
    components = n

    for left, right in edges:
        # Only successful unions reduce the number of connected components.
        if uf.union(left, right):
            components -= 1

    return components
