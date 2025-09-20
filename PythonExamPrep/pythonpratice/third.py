#string handling

college = 'presidency'

stlen = len(college)
print("The college has the ",stlen,"Letters")

print(college[3:])
print(college[:3])
print(college[0])

for i in college:
    print(i)

count = college.count("e")
print("College number of e",count)
inst = 'presidency college'
print(inst.replace("college","university"))

print(college.find('side'))
