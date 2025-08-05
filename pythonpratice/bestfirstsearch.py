from queue import PriorityQueue as PQ

def bestfs(g, s, e):
    v, q = set(), PQ()
    q.put((0, s))
    while not q.empty():
        _, n = q.get()
        if n in v: continue
        print(n)
        if n == e: return True
        v.add(n)
        [q.put((int(c), x)) for x, c in g[n].items() if x not in v]
    return False

g = {'A': {'B': '3', 'C': '6'}, 'B': {'D': '2', 'E': '1'},
     'C': {'F': '5'}, 'D': {}, 'E': {'F': '4'}, 'F': {}}

print("Path exists", bestfs(g, 'A', 'F'))
