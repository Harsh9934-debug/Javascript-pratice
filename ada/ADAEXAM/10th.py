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
