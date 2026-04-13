arr = list(map(int, input("Enter elements: ").split()))
for i in range(len(arr)):
    m = min(range(i, len(arr)), key=arr.__getitem__)
    arr[i], arr[m] = arr[m], arr[i]
print("Sorted:", arr)