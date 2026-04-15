def quick_sort(arr):
   if len(arr)<=1:
      return arr
   else:
      pivot = arr[len(arr)//2]
      left = [x for x in arr if x<pivot]
      right = [x for x in arr if x>pivot]
      return quick_sort(left)+[pivot]+quick_sort(right)
elements = list(map(int,input("Enter the elements:").split()))
print("Sorted element",quick_sort(elements))

