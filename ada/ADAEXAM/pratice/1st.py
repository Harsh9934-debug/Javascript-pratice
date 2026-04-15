arr=list(map(int,input("Enter the number of elements in the array").split()))
x=int(input("Enter the element to search"))
print(next((i for i,v in enumerate(arr) if v==x),-1))