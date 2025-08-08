# List operation 

a = [10,20,30,40,50]
print("List elements are: ",a)

a.insert(1,15)
a.append(60)
print("The length of a is ",len(a))
a.remove(30)
print("After the removal of (30) is :",a)
popped_val = a.pop(1)
print("Popped element is:",popped_val)
print("After pop(1)",a)
del a[0]
print("After the removal ",a)
a.clear()
print(a)