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
"""
DETAILED WORKING OF THE ALGORITHM (Greedy Job Sequencing with Deadlines):

1. Greedy Prioritization Sorting:
   - The first and most essential step dictates sorting the jobs array completely in descending order relying squarely on `Profit`. The algorithm MUST lock in the absolute highest monetary options globally.

2. Structural Limits:
   - Computes exactly what the maximal deadline is outright to instantiate `slots`. The `slots` act as a static grid calendar ensuring jobs run inside bounds.

3. The Greedy Choice Placement:
   - Iterates iteratively through sorted high-profit sequences!
   - Crucially scans the timeline `range(...)` inside-out completely BACKWARDS from the job's defined deadline integer down to 0. 
   - We place the job perfectly into its most furthest-right *empty* slot `-1` immediately without wasting an earlier time slot, actively retaining premium open areas for overlapping jobs!
   - Adjusts total net-sum `profit` statically while blocking the schedule index.
"""
