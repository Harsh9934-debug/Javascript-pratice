# Program to demonstrate the dictionary 

courses = {'Python':'BCA', 'ACA':'BCOM','IBE':'BBA'}

for keys,value in courses.items():
    print("The key is ",keys,"and the value is ",value)

for keys in courses.keys():
    print("The key value is ",keys)


for keys in courses.values():
    print("The value is ",value)
