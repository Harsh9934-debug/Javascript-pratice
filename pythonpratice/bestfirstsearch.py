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

graph = {
    'A':{'B':'3','C':'6'},
    'B':{'D':'2','E':'1'},
    'C':{'F':'5'},
    'D':{},
    'E':{'F':'4'},
    'F':{}
}

start_node = 'A'
goal_node = 'F'
result = bestfs(graph,start_node,goal_node)
print("Path exists",result)