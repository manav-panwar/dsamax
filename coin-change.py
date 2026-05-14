def worker(coins, amount):

    n = amount
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(1, n+1):
            if i - coin >= 0: 
                dp[i] = min(dp[i], 1 + dp[i - coin])
            else: continue

    return dp[n] if dp[n] != float('inf') else -1

