def binary_search(arr, x):
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
arr = list(map(int, input("Enter elements: ").split()))
arr.sort()
key = int(input("Enter element to search: "))
result = binary_search(arr, key)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")