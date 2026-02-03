#write a program to implement the linear serarch using divide and conquer

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = list(map(int, input("Enter elements with the spacing: ").split()))
x = int(input("Enter the element to search: "))
result = linear_search(arr, x)
if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")
