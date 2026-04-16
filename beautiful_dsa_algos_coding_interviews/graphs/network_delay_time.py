import heapq
from typing import List


def network_delay_time(times: List[List[int]], n: int, k: int) -> int:
    """
    Return how long it takes for a signal from k to reach all nodes.

    Time complexity: O((V + E) log V) because Dijkstra relaxes each edge while
    heap operations are logarithmic in the number of nodes tracked.
    Space complexity: O(V + E) for the adjacency list, heap, and best-distance map.
    """
    graph = [[] for _ in range(n + 1)]
    for source, target, weight in times:
        graph[source].append((target, weight))

    min_heap = [(0, k)]
    best_time = {}

    while min_heap:
        elapsed, node = heapq.heappop(min_heap)
        if node in best_time:
            continue

        best_time[node] = elapsed

        for neighbor, weight in graph[node]:
            if neighbor not in best_time:
                heapq.heappush(min_heap, (elapsed + weight, neighbor))

    if len(best_time) != n:
        return -1

    return max(best_time.values())
