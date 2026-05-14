def worker(n):

    dp = [float('inf')] * (n+1)
    dp[0] = 0
    
    for number in range(1, n+1):
        j = 1
        while j*j <= number:
            dp[number] = min(dp[number], 1 + dp[number - j*j])
            j +=1
    
    return dp[n]
