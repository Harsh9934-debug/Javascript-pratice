def solve(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)
    slots = [-1] * max(j[1] for j in jobs)
    profit = 0

    for job, deadline, p in jobs:
        for i in range(min(len(slots), deadline) - 1, -1, -1):
            if slots[i] == -1:
                slots[i], profit = job, profit + p
                break

    print("Sequence:", " -> ".join(j for j in slots if j != -1))
    print("Profit:", profit)

if __name__ == "__main__":
    jobs = [("J1", 2, 100), ("J2", 1, 19), ("J3", 2, 27), ("J4", 1, 25), ("J5", 3, 15)]
    solve(jobs)
