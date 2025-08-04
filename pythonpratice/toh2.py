def toh (n,start,aux,end):
    if n==1:
        print(f"Move the disk 1 form the {start} to {end}")
        return
    toh(n-1,start,aux,end)
    print(f"move the {n} disk from the {start} to {end}")
    toh(n-1,aux,end,start)
try:
    n = int(input("Enter the number of the disks: "))
    if(n<=0):
        print("Enter an positive interger")
    else:
        print("Disks are moving in the following way")
        toh(n,'A','B','C')
except ValueError:
    print("Enter the valid input")