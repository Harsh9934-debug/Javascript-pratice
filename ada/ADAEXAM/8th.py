g = [[0,5,999],
     [999,0,3],
     [2,999,0]]

for k in range(3):
    for i in range(3):
        for j in range(3):
            g[i][j] = min(g[i][j], g[i][k] + g[k][j])

print(g)