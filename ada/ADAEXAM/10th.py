def solve(graph, m, color, v=0):
    if v == len(graph): return True
    for c in range(1, m + 1):
        if all(color[i] != c for i, adj in enumerate(graph[v]) if adj):
            color[v] = c
            if solve(graph, m, color, v + 1): return True
            color[v] = 0
    return False

if __name__ == "__main__":
    graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    color = [0] * len(graph)
    print("Solution:", *color) if solve(graph, 3, color) else print("No solution")