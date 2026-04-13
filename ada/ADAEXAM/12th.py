def knapsack(W, wt, val):
    dp = [0] * (W + 1)
    for w, v in zip(wt, val):
        for j in range(W, w - 1, -1):
            dp[j] = max(dp[j], dp[j - w] + v)
    return dp[W]

print("Max value:", knapsack(50, [10, 20, 30], [60, 100, 120]))