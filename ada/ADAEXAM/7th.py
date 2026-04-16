g = [[0,2,0,6], [2,0,3,8], [0,3,0,0], [6,8,0,0]]
s = [1,0,0,0]
for _ in range(3):
    m, x, y = 999, 0, 0
    for i in range(4):
        for j in range(4):
            if s[i] and not s[j] and 0 < g[i][j] < m:
                m, x, y = g[i][j], i, j
    print(x, y, m)
    s[y] = 1