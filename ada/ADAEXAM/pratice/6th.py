def merge_sort(arr):
    if len(arr)<2:
        return arr
    l = merge_sort(arr[:len(arr)//2])
    r = merge_sort(arr[len(arr)//2:])
    return sorted(l+r)

arr = list(map(int,input("Enter the elements").split()))
print("Sorted:",merge_sort(arr))