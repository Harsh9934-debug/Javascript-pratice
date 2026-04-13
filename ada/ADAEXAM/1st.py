arr = list(map(int, input("Enter elements: ").split()))
x = int(input("Enter element to search: "))
print(next((i for i, v in enumerate(arr) if v == x), -1))