jobs = [('A',2,100), ('B',1,50), ('C',2,10)]
jobs.sort(key=lambda x: x[2], reverse=True)
slot = [0,0]
total_profit = 0
for j in jobs:
    for i in range(j[1]-1, -1, -1):
        if slot[i] == 0:
            slot[i] = j[0]
            total_profit += j[2]
            break
print("Sequence:", slot)
print("Total Profit:", total_profit)