def knapsack(capacity,weight,value):
    dp=[0]*(capacity+1)
    for weight,value in zip(weight,value):
        for curr_cap in range(capacity,weight-1,-1):
            dp[curr_cap]=max(dp[curr_cap],dp[curr_cap-weight]+value)
    return dp[capacity]
print("Maximum Value",knapsack(50,[10,20,30],[60,100,120]))