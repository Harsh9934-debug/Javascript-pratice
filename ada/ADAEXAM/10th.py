g = [[0,1,1,1],
     [1,0,1,0],
     [1,1,0,1],
     [1,0,1,0]]
c = [0,0,0,0]
for v in range(4):
    for col in [1,2,3]:
        ok = 1
        for i in range(4):
            if g[v][i] == 1 and c[i] == col:
                ok = 0
        if ok:
            c[v] = col
            break
print(c)





