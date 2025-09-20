#list operation 

a=[1,2,3,4,5]
b=['Apple','Banana','Cherry']
c=[1,'Apple',3.14]

print(a)
print(b)
print(c)

print(a[0])
print(a[-1])

for i in a:
    print(i)

a.append(20)
print(a)

a.remove(20)
print(a)

a.extend([15,20,30])
print(a)


a.pop(2)
print(a)

a.clear()
print(a)