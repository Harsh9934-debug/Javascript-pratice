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
"""
DETAILED WORKING OF THE ALGORITHM (Prim's MST):

1. Initialization:
   - `key`: Tracks minimal edge weights initialized to infinity. The root is given weight 0.
   - `parent`: Stores the MST structure to backtrace the parent of each node.
   - `mst`: Array identifying exactly which nodes have been cemented into the final Minimum Spanning Tree.

2. Picking the Root:
   - The loop spins `V` times. In each iteration, it picks node `u` containing the absolute minimal weight globally which is NOT currently inside the `mst`.

3. Exploration & Updates:
   - Marks `u` True inside the MST track.
   - For every adjacent vertex `v` physically touching `u`:
     if `v` is NOT in the MST yet and the touching edge `u-v` is LIGHTER than `v`'s current best known `key`, we aggressively update `key[v]` to ensure the minimal link is preserved!

4. Result Output:
   - Calculates the net mathematical sum over the `graph` directly linking to the optimal paths tracked inside `parent`.
"""
