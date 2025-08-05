from queue import PriorityQueue

def bestfs(g, s, goal):
    v, q = set(), PriorityQueue()
    q.put((0, s))
    while not q.empty():
        _, n = q.get()
        if n in v: continue
        print(n)
        if n == goal: return True
        v.add(n)
        for nei, c in g[n].items():
            if nei not in v: q.put((int(c), nei))
    return False

graph = {
    'A': {'B': '3', 'C': '6'},
    'B': {'D': '2', 'E': '1'},
    'C': {'F': '5'},
    'D': {}, 'E': {'F': '4'}, 'F': {}
}

print("Path exists", bestfs(graph, 'A', 'F'))
