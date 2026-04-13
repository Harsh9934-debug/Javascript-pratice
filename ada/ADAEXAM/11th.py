def job_scheduling(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)
    slots = [-1] * max(j[1] for j in jobs)
    profit = sum(p for _, _, p in jobs)
    for job, deadline, _ in jobs:
        for i in range(min(len(slots), deadline) - 1, -1, -1):
            if slots[i] == -1:
                slots[i] = job
                break
            else: profit -= _
    print("Sequence:", " -> ".join(j for j in slots if j != -1))
    print("Profit:", profit)

jobs = [("J1", 2, 100), ("J2", 1, 19), ("J3", 2, 27), ("J4", 1, 25), ("J5", 3, 15)]
job_scheduling(jobs)