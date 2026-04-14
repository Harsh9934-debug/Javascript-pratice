def quick_sort(arr):
    if len(arr) <= 1: return arr
    p = arr[len(arr) // 2]
    return quick_sort([x for x in arr if x < p]) + [x for x in arr if x == p] + quick_sort([x for x in arr if x > p])

arr = list(map(int, input("Enter elements: ").split()))
print("Sorted:", quick_sort(arr))
"""
DETAILED WORKING OF THE ALGORITHM (Quick Sort):

1. Base Case:
   - If the array contains 1 or fewer elements, it is implicitly already sorted, so return `arr`.

2. Pivot Selection:
   - A pivot element `p` is chosen from the exact middle of the array using `len(arr) // 2`.

3. Partitioning:
   - The algorithm splits elements into 3 distinct lists via list comprehensions:
     - The left block: all elements smaller than `p`.
     - The middle block: all elements explicitly equal to `p`.
     - The right block: all elements strictly larger than `p`.

4. Recursive Tying:
   - The method recursively sorts the left and right groups, and finally concatenates them: `SortedLeft + Middle + SortedRight` which returns the completed, ordered structure!
"""
