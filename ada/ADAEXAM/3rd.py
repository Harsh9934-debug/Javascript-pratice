def toh(n, src, dst, aux):
    if n == 0: return
    toh(n - 1, src, aux, dst)
    print(f"Move disk {n} from {src} to {dst}")
    toh(n - 1, aux, dst, src)

toh(int(input("Enter disks: ")), 'A', 'C', 'B')
"""
DETAILED WORKING OF THE ALGORITHM (Tower of Hanoi):

1. Base Condition:
   - If the number of disks `n` is exactly 0, there are no disks to move, so it purely returns.

2. Recursive Step 1 (Sub-problem):
   - `toh(n - 1, src, aux, dst)` shifts the top `n-1` disks from the Source rod to the Auxiliary rod. This temporarily clears the path for the largest disk.

3. Core Move:
   - After the `n-1` disks are out of the way, the largest disk `n` is physically moved directly from the Source to Destination.

4. Recursive Step 2 (Restoration):
   - `toh(n - 1, aux, dst, src)` takes those `n-1` disks from the Auxiliary rod and shifts them onto the Destination rod over the largest disk, successfully concluding the full stack transfer!
"""
