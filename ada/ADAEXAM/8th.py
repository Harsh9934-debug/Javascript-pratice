import sys
INF = sys.maxsize
def floyd_warshall(graph):
    V = len(graph)
    dist = [[graph[i][j] for j in range(V)] for i in range(V)]
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] != INF and dist[k][j] != INF:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    for i in range(V):
        print(" ".join(f"{'INF' if d == INF else d:4}" for d in dist[i]))
if __name__ == "__main__":
    graph = [
        [0, 10, 6, 5],
        [10, 0, 9999, 15],
        [6, 9999, 0, 4],
        [5, 15, 4, 0]
    ]
    floyd_warshall(graph)