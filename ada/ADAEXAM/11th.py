def job_scheduling(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)
    max_deadline = 0
    for job in jobs:
        if job[1] > max_deadline:
            max_deadline = job[1]
    slots = [-1] * max_deadline
    total_profit = 0
    for job in jobs:
        job_id = job[0]
        deadline = job[1]
        profit = job[2]
        start_slot = min(max_deadline, deadline) - 1
        for i in range(start_slot, -1, -1):
            if slots[i] == -1:
                slots[i] = job_id
                total_profit += profit
                break
    scheduled_jobs = []
    for s in slots:
        if s != -1:
            scheduled_jobs.append(s)
    print("Scheduled Sequence:", " -> ".join(scheduled_jobs))
    print("Total Profit:", total_profit)

jobs = [("J1", 2, 100), ("J2", 1, 19), ("J3", 2, 27), ("J4", 1, 25), ("J5", 3, 15)]
job_scheduling(jobs)
