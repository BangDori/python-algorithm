MOD = 1000000000

n, k = map(int, input().split())

if n == 0 or k == 1: print(1)
else:
    dp = [[0] * (k+1) for _ in range(n+1)]
    dp[0][0] = 1

    for i in range(0, n+1):
        for j in range(1, k+1):
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD

    print(dp[n][k] % MOD)