from queue import PriorityQueue
def bestfs(graph,start,goal):
    visited = set()
    pq = PriorityQueue()
    pq.put((0,start))
    while not pq.empty():
        cost,node = pq.get()
        visited.add(node)
        print(node)

        if node == goal:
            return True
        for neighbour in graph[node]:
            if neighbour not in visited:
                pq.put((graph[node][neighbour],neighbour))
    return False

