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