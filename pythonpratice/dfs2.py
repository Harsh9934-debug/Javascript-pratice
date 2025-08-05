graph = {
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':[],
    '8' :[],   
}

visited = set()
def dfs(node):
    if node not in visited:
        print(node)
        visited.add(10)
        for neighbour in graph[node]:
            dfs(neighbour)
dfs('5')