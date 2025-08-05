from queue import PriorityQueue

# Define the graph as an adjacency list
graph = {
    'S': ['A', 'B'],
    'A': ['C'],
    'B': ['D', 'E'],
    'C': [],
    'D': [],
    'E': ['G'],
    'G': []
}

# Define the heuristic (h(n)) for each node
heuristic = {
    'S': 5,
    'A': 4,
    'B': 3,
    'C': 2,
    'D': 6,
    'E': 1,
    'G': 0
}

# Best First Search algorithm
def best_first_search(start, goal):
    visited = set()
    pq = PriorityQueue()
    pq.put((heuristic[start], start))

    while not pq.empty():
        _, current = pq.get()
        if current in visited:
            continue
        print(current, end=" ")
        visited.add(current)

        if current == goal:
            break

        for neighbor in graph[current]:
            if neighbor not in visited:
                pq.put((heuristic[neighbor], neighbor))

# Run the search from S to G
best_first_search('S', 'G')
