def toh(n,start,aux,end):
    if n==1:
        print(f"move the 1 disk from {start} to {end}")
        return
    toh(n-1,start,end,aux)
    print(f"move the {n} disk from {start} to {end}")
    toh(n-1,aux,start,end)
try:
    n=int(input("Enter the number of disks"))
    if n <= 0:
        print("Enter the positive number of disks")
    else:
        print("Disks are moving in the folliwing manners")
        toh(n,'A','B','C')
except ValueError:
    print("Invalid input!")