import sys
input = sys.stdin.readline
MOD = 1000000000

n = int(input())
dp = [[1 for _ in range(10)] for _ in range(n)]
dp[0][0] = 0

for i in range(1, n):
    dp[i][0] = dp[i-1][1]
    for j in range(1, 9):
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % MOD
    dp[i][9] = dp[i-1][8]

print(sum(dp[n-1]) % MOD)