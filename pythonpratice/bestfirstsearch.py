from queue import PriorityQueue
def bestfs(graph,start,goal):
    visited = set()
    pq = PriorityQueue()
    pq.put((0,start))
    while not pq.empty():
        cost,node = pq.get()
        visited.add(node)
        print(node)

        