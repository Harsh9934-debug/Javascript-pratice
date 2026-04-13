def knapsack(W, wt, val):
    dp = [0] * (W + 1)
    for w_i, v_i in zip(wt, val):
        for w in range(W, w_i - 1, -1):
            dp[w] = max(dp[w], v_i + dp[w - w_i])
    return dp[W]

print("Max val =", knapsack(50, [10, 20, 30], [60, 100, 120]))