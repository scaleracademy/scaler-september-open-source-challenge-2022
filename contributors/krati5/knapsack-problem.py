
def dynamic_programming_recursive_knapsack(weight, value, W, n):
    
    dp = [[-1 for j in range(W+1)] for i in range(n+1)]

    for j in range(W+1):
        dp[0][j] = 0
    
    for i in range(n+1):
        dp[i][0] = 0
        
    for i in range(1, n+1):
        for j in range(1, W+1):
            
            if weight[i-1] <= j:
                dp[i][j] = max(value[i-1] + dp[i-1][j-weight[i-1]],dp[i-1][j])
                
            else:
                dp[i][j] = dp[i-1][j]
                
    return dp[n][W]


if __name__=='__main__':
    value = [60, 100, 120]
    weight = [10, 20, 30]
    n = len(value)
    
    W = 50 # Capacity
    print("Dynamic Programming Top-Down Approach: ", dynamic_programming_recursive_knapsack(weight, value, W, n))
    