arr = list(map(int, input("Enter elements: ").split()))
for i in range(len(arr)):
    m = min(range(i, len(arr)), key=arr.__getitem__)
    arr[i], arr[m] = arr[m], arr[i]
print("Sorted:", arr)
"""
DETAILED WORKING OF THE ALGORITHM (Selection Sort):

1. Iteration:
   - The outer loop steps through each index `i` of the array. The idea is to find the smallest element in the unsorted portion and bring it to `i`.

2. Finding the Minimum:
   - `min(range(i, len(arr)), key=arr.__getitem__)` acts as an inner loop that strictly finds the index `m` containing the absolute minimum value from the remaining unsorted sub-array.

3. Swapping:
   - `arr[i], arr[m] = arr[m], arr[i]` cleanly swaps the element at `i` (the start of the unsorted part) with the minimum found element at `m`.
   - By the time `i` finishes iterating over the bounds, the entire array is perfectly sorted!
"""
