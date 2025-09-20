# Program to demonstrate the operation in tuple 

tp1 = ('F','1','a','b','b','e','r','g','a','s','t','e','d')
tp1 = tp1+('1',)
print(tp1)

s = ''.join(tp1)
print(s)

t = tp1 [3:5]
print(t)

count = tp1.count('e')
print("Count of e is ",count)

print('r' in tp1)

lst =  list(tp1)
print(lst)

tp1 = tp1[:3] + tp1[7:]
print(tp1)