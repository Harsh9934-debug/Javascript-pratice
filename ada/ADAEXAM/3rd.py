#write a python program to implement the tower of hanoi using recursion 

def toh(n, source, destination, auxiliary):
    if n==1:
        print("Move disk 1 from source",source,"to destination",destination)
        return
    toh(n-1, source, auxiliary, destination)
    print("Move disk",n,"from source",source,"to destination",destination)
    toh(n-1, auxiliary, destination, source)
    
n=int(input("Enter the number of disks: "))
toh(n,'A','C','B')