def toh(n,src,des,aux):
    if n==0:
        return
    toh(n-1,src,aux,des)
    print(f"Move the disk {n} from {src} to {des}")
    toh(n-1,aux,des,src)

toh(int(input("Enter the number of disks")),"A","C","B")