def toh(n,start,aux,end):
    if n==1:
        print(f"move the 1 disk from {start} to {end}")
        return
    toh(n-1,start,aux,end)
    print(f"move the {n} disk from the {start} to {aux}")
    toh(n-1,aux,end,start)
try:
    n=int(input("Enter the number of disks"))
    if n <= 0:
        print("Enter the positive number of disks")
    else:
        print("Disks are moving in the folliwing manners")
        toh(n,'A','B','C')
except ValueError:
    print("Invalid input!")