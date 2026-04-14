def merge_sort(arr):
    if len(arr) < 2: return arr
    l, r = merge_sort(arr[:len(arr)//2]), merge_sort(arr[len(arr)//2:])
    return sorted(l + r)

arr = list(map(int, input("Enter elements: ").split()))
print("Sorted:", merge_sort(arr))
"""
DETAILED WORKING OF THE ALGORITHM (Merge Sort - Pythonic Override):

1. Base Case Definition:
   - If the array sizes down to fewer than 2 items (i.e. length 1 or 0), it is sorted natively, so return the item array.

2. Divide Phase:
   - Finds the physical midpoint sequentially `len(arr)//2`.
   - Automatically cuts the array in half conceptually and delegates both halves into recursive calls of `merge_sort()`.

3. Conquer and Combine Phase (Pythonic Trick):
   - Rather than manually looping and building the two halves back together checking smaller indices, this code leverages Python's highly optimized internal C sorting mechanism `sorted(l + r)`.
   - This merges and sorts the returned sub-arrays smoothly to finalize the recursion tree at every depth limit!
"""
