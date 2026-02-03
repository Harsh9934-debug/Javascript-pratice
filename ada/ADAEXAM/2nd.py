#write a program to implement the binary search using divide and conquer

def binary_search(arr, low, high, x):
    if low>high:
        return -1
    mid = (low+high)//2
    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
        return binary_search(arr, low, mid-1, x)
    else:
        return binary_search(arr, mid+1, high, x)
arr = list(map(int, input("Enter elements with the spacing: ").split()))
key=int(input("Enter the element to search: "))
result = binary_search(arr, 0, len(arr)-1, key)
if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")