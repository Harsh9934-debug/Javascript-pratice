def quick_sort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivort = arr[len(arr)//2]
        left = [x for x in arr if x<pivort]
        right = [x for x in arr if x>pivort]
        return quick_sort(left) + [pivort] + quick_sort(right)

arr = list(map(int,input("Enter the elements").split()))
print("Sorted elements:",quick_sort(arr))
