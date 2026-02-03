#write a python program to implement the quick sort

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid  = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)

arr = list(map(int, input("Enter elements with spacing: ").split()))
print("Sorted array:", quick_sort(arr))
