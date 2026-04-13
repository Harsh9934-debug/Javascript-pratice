import sys

def prim(graph):
    V = len(graph)
    key, parent, mst_set = [sys.maxsize] * V, [-1] * V, [False] * V
    key[0] = 0

    for _ in range(V):
        u = min((v for v in range(V) if not mst_set[v]), key=lambda v: key[v])
        mst_set[u] = True
        for v in range(V):
            if 0 < graph[u][v] < key[v] and not mst_set[v]:
                key[v], parent[v] = graph[u][v], u

    print("Edge \tWeight")
    print(f"Total Weight: {sum(graph[i][parent[i]] for i in range(1, V))}")
    for i in range(1, V): 
        print(f"{parent[i]} - {i} \t{graph[i][parent[i]]}")

if __name__ == "__main__":
    graph = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0]
    ]
    prim(graph)
