class UnionFind:
    """
    Disjoint-set union with path compression and union by rank.

    Amortized time complexity: nearly O(1), often written as O(alpha(N)).
    Space complexity: O(N)
    """

    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, node: int) -> int:
        if self.parent[node] != node:
            # Path compression flattens the tree so future finds are faster.
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, left: int, right: int) -> bool:
        root_left = self.find(left)
        root_right = self.find(right)

        if root_left == root_right:
            return False

        # Union by rank keeps the shallower tree under the deeper one.
        if self.rank[root_left] < self.rank[root_right]:
            self.parent[root_left] = root_right
        elif self.rank[root_left] > self.rank[root_right]:
            self.parent[root_right] = root_left
        else:
            self.parent[root_right] = root_left
            self.rank[root_left] += 1

        return True
