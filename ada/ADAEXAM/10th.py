def graph_color(graph, m, color, v=0):
    if v == len(graph): return True
    for c in range(1, m + 1):
        if all(not adj or color[i] != c for i, adj in enumerate(graph[v])):
            color[v] = c
            if graph_color(graph, m, color, v + 1): return True
            color[v] = 0
    return False

graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
color = [0] * 4
print("Solution:" if graph_color(graph, 3, color) else "No solution", *color)
"""
DETAILED WORKING OF THE ALGORITHM (Graph Coloring using Backtracking):

1. The Backtracking State Check (`all` optimization):
   - To make sure no two adjacent nodes possess identical colors, the single `all()` statement ensures that for every adjacent node `i` connecting to `v`, if it *is* an edge `adj`, its existing color MUST NOT actively equal our current test color `c`.

2. Recursive Testing Engine (`graph_color`):
   - It begins iteratively assigning colors `1` to `m` onto vertex `v`.
   - If the color successfully validates through the `all()` safety check above, it assigns `color[v] = c`.
   - It then immediately recursion dives deeper into `v + 1`. If the rest of the nodes succeed through this chain, it natively bubbles `True` all the way out successfully completing the maze!

3. The "Backtrack" Pivot:
   - If `v + 1` mathematically fails on any color combination, it returns physically `False`. The current vertex forcefully rejects that path, wipes its color `color[v] = 0` (undoes action), and spins up the next color iteration `c+1` dynamically to retry newly formulated paths!
"""
