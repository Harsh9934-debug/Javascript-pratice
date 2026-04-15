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