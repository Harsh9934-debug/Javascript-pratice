def knapsack(capacity, weights, values):
    dp = [0] * (capacity + 1)
    for weight, value in zip(weights, values):
        for curr_cap in range(capacity, weight - 1, -1):
            dp[curr_cap] = max(dp[curr_cap], dp[curr_cap - weight] + value)
    return dp[capacity]

print("Max value:", knapsack(50, [10, 20, 30], [60, 100, 120]))

"""
DETAILED WORKING OF THE ALGORITHM:

1. Initialization:
   - We create a 1D array `dp` of size `capacity + 1` initialized to 0.
   - `dp[c]` tracks the maximum value that can be achieved using exactly capacity `c`.

2. Iterating through the items:
   - We loop through every item one by one, extracting its `weight` and `value`.

3. Iterating BACKWARDS through capacities for each item:
   - For every item, we iterate `curr_cap` backwards from the maximum `capacity` down to the item's own `weight`.
   - WHY BACKWARDS? If we looped forwards, an updated `dp[curr_cap - weight]` (which would have already included the current item) could be used to calculate a larger `dp[curr_cap]`. This would simulate using the *same* item multiple times.
   - By looping backwards, `dp[curr_cap - weight]` strictly references the DP state from the *previous* item's iteration, ensuring this item is only used exactly once (0/1 Knapsack rule).

4. The Core Choice:
   - dp[curr_cap] = max(dp[curr_cap], dp[curr_cap - weight] + value)
   - Exclude the item: Keep the previous best value computed for this capacity `dp[curr_cap]`.
   - Include the item: Add this item's `value` to the best value computed for the remaining capacity `dp[curr_cap - weight]`.
   - We take the maximum of these two options.

5. Final Result:
   - When all items and capacities are processed, `dp[capacity]` stores the maximum possible total value for the knapsack.
"""
