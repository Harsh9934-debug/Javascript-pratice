#write a python program to implement the merge sort

def merge_sort(arr):
    if len(arr) < 2: return arr
    m = len(arr) // 2
    l, r, i, j, res = merge_sort(arr[:m]), merge_sort(arr[m:]), 0, 0, []
    while i < len(l) and j < len(r):
        if l[i] < r[j]: res.append(l[i]); i += 1
        else: res.append(r[j]); j += 1
    return res + l[i:] + r[j:]
arr = list(map(int, input("Enter elements with the spacing: ").split()))
print("Sorted array:", merge_sort(arr))
