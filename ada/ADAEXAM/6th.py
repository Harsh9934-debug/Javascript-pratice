def merge_sort(arr):
    if len(arr) < 2: return arr
    l, r = merge_sort(arr[:len(arr)//2]), merge_sort(arr[len(arr)//2:])
    return sorted(l + r)

arr = list(map(int, input("Enter elements: ").split()))
print("Sorted:", merge_sort(arr))
