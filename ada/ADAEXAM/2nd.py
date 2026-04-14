def binary_search(arr, x):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == x: return mid
        lo, hi = (mid + 1, hi) if arr[mid] < x else (lo, mid - 1)
    return -1

arr = sorted(map(int, input("Enter elements: ").split()))
key = int(input("Enter element to search: "))
print(binary_search(arr, key))
"""
DETAILED WORKING OF THE ALGORITHM (Binary Search):

1. Initialization:
   - Requires a SORTED array. 
   - `lo` and `hi` pointers are initialized to the start and end indices.

2. Loop Execution:
   - Finds the middle element `mid`.
   - If `arr[mid] == x`, the target is found and we return `mid`.

3. Search Space Halving:
   - If the middle element is less than `x`, the target must be on the right, so we update `lo = mid + 1`.
   - If the middle element is greater than `x`, the target must be on the left, so we update `hi = mid - 1`.

4. Completion:
   - The loop continually halves the array space achieving O(log n) time.
   - If the loop exhausts and `lo > hi`, the target doesn't exist, returning `-1`.
"""
