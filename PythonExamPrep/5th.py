#Programs to deminstrate the list operation in pythhon

a = [1,2,3,4,5]
b =['Apple','Banana','Cherry']
c = [1,'Hello',3.14,True]

print(a)
print(b)
print(c)
print(a[1])
print(a[0])
a.append(10)
a.insert(0,5)
print("After inserting (0,5): ",a)
a.extend([15,20,25])
print("After expanding: ",a)
a[1] = 100
print(a)
a.remove(100)
print("After removing (100) :",a)
for i in a :
    print(i)