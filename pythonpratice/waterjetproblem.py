from collections import deque

def water_jug(j1, j2, target):
    q, visited = deque([(0, 0)]), set()

    while q:
        a, b = q.popleft()
        if (a, b) in visited: continue
        visited.add((a, b))
        print(f"Jug1: {a}, Jug2: {b}")
        if a == target or b == target:
            print("✅ Target reached!")
            return

        q.extend([
            (j1, b), (a, j2), (0, b), (a, 0),
            (a - min(a, j2 - b), b + min(a, j2 - b)),
            (a + min(b, j1 - a), b - min(b, j1 - a))
        ])

water_jug(4, 3, 2)
