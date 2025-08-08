#program to demonstrate the dictionary

course = {'BCA':'Pyhton','BBA':'English','BCOM':'Bussiness'}

for key,value in course.items():
    print("The key value is :",key," and the courses in it is:",value)

for key in course.keys():
    print(key)

for key in course.values():
    print(key)