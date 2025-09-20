#String Handling

college = "presidency"
stlen = len(college)
print("college has ",stlen,"letters")
print(college[:3])
print(college[2:5])
for i in college:
    print(i)
print(college.lower())
print(college.upper())
countletters = college.count("e")
print(countletters)
subst = college.find("side")
print(subst)
print(college.isalnum())
print(college.replace("presidency","college"))