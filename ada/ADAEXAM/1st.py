arr = list(map(int, input("Enter elements: ").split()))
x = int(input("Enter element to search: "))
print(next((i for i, v in enumerate(arr) if v == x), -1))

"""
DETAILED WORKING OF THE ALGORITHM (Linear Search):

1. Initialization:
   - Evaluates each element inside the target sequence `arr`.
   - `enumerate()` keeps track of both the index `i` and the value `v`.

2. Generator Expression:
   - `(i for i, v in enumerate(arr) if v == x)` generates the indices where the value matches the search key `x`.

3. Result Processing:
   - `next()` fetches the very first matching index from the generator.
   - If the generator is empty (element not found), it returns the default fallback value `-1`!
"""
