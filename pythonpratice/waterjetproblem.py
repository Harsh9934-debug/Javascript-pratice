from collections import defaultdict
jug1, jug2, target = 4, 3, 2
visited = defaultdict(bool)
def solve(x, y):
    if (x == target and y == 0) or (x == 0 and y == target):
        print(f"({x}, {y})")
        return True
    if visited[(x, y)]:
        return False
    print(f"({x}, {y})")
    visited[(x, y)] = True
    return (solve(0, y) or  
            solve(x, 0) or
            solve(jug1, y) or
            solve(x, jug2) or
            solve(x + min(y, jug1 - x), y - min(y, jug1 - x)) or
            solve(x - min(x, jug2 - y), y + min(x, jug2 - y)))
print("Steps:")
solve(0, 0)
