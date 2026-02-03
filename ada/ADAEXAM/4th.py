#write a python program to sort the given set if number using the selection sort algorithm

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
arr = list(map(int, input("Enter elements with the spacing: ").split()))
print("Sorted array:", selection_sort(arr))
