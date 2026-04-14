def floyd_warshall(graph):
    V = len(graph)
    dist = [row[:] for row in graph]
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    for row in dist:
        print(" ".join(f"{d:4}" for d in row))

graph = [[0, 10, 6, 5], [10, 0, 9999, 15], [6, 9999, 0, 4], [5, 15, 4, 0]]
floyd_warshall(graph)
"""
DETAILED WORKING OF THE ALGORITHM (Floyd-Warshall):

1. Initializing State DP:
   - It clones the initial adjacency graph cleanly using `[row[:] for row in graph]`. This duplicate serves as the running optimal distance matrix `dist`.

2. The 3-Dimensional Core Loops:
   - The algorithm steps through exactly 3 loops: `k`, `i`, and `j`. 
   - Outer loop `k` acts as the "intermediate" bridging node.
   - Loop `i` acts as the source node, and `j` acts as the destination node.

3. The Optimal Bridge Condition:
   - `dist[i][k] + dist[k][j] < dist[i][j]` checks if rerouting the path from `i -> j` to temporarily bounce through `k` makes the trip physically shorter.
   - If it is shorter, the existing shortest-path value for `dist[i][j]` is permanently overwritten.

4. Asymptotic Completion:
   - Because `k` checks every single node universally from source to dest intersections, evaluating all combinations guarantees O(V^3) all-pairs shortest paths globally!
"""
