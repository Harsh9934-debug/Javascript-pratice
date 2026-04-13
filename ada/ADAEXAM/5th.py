def quick_sort(arr):
    if len(arr) <= 1: return arr
    p = arr[len(arr) // 2]
    return quick_sort([x for x in arr if x < p]) + [x for x in arr if x == p] + quick_sort([x for x in arr if x > p])

arr = list(map(int, input("Enter elements: ").split()))
print("Sorted:", quick_sort(arr))