def toh(n, src, dst, aux):
    if n == 0: return
    toh(n - 1, src, aux, dst)
    print(f"Move disk {n} from {src} to {dst}")
    toh(n - 1, aux, dst, src)

toh(int(input("Enter disks: ")), 'A', 'C', 'B')