graph = {
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[ ],
    '4':['8'],
    '8':[],
}
visited = []
queue = ['5']
while queue:
    node = queue.pop(0)
    if node not  in visited:
        print(node)
        visited.append(node)
        queue +=graph[node]
        