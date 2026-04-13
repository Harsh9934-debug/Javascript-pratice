def prim(graph):
    V = len(graph)
    key, parent, mst = [float('inf')] * V, [-1] * V, [False] * V
    key[0] = 0
    for _ in range(V):
        u = min((v for v in range(V) if not mst[v]), key=lambda v: key[v])
        mst[u] = True
        for v in range(V):
            if 0 < graph[u][v] < key[v] and not mst[v]:
                key[v], parent[v] = graph[u][v], u
    print(f"Total Weight: {sum(graph[i][parent[i]] for i in range(1, V))}")

graph = [[0, 2, 0, 6, 0], [2, 0, 3, 8, 5], [0, 3, 0, 0, 7], [6, 8, 0, 0, 9], [0, 5, 7, 9, 0]]
prim(graph)