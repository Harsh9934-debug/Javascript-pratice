def toh(n,start,aux,end):
    if n==1:
        print(f"move the 1 disks form the {start} to {end} ")
        return
    toh(n-1,start,aux,end)
    print(f"move the {n} disks from the {start} to {end}")
    toh(n-1,aux,end,start)

try:
    n=int(input("Enter the number of the disks in the tower"))
    if (n <= 0):
        print("enter the positive interger")
    else:
        print(f"Soling for the tower of hanoi for {n} disks")
        toh(n,'A','B','C')
except ValueError:
    print("Invalid input enter the valid interger")