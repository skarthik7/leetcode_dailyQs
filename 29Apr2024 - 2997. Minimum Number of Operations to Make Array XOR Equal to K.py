def minOperations(nums, k):
    n = len(nums)
    dp = [[float('inf')] * 1024 for _ in range(n+1)]
    dp[0][0] = 0

    for i in range(1, n+1):
        x = nums[i-1]
        for j in range(1024):
            # calculate the cost of flipping bits in x to achieve the desired XOR
            cost = bin(x^j).count('1')
            dp[i][j] = min(dp[i-1][j^x] + cost, dp[i-1][j])

    return dp[n][k] if dp[n][k] != float('inf') else -1