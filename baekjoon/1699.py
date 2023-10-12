import sys
input = sys.stdin.readline

N = int(input())
dp = [0 for _ in range(100001)]
dp[1] = 1
dp[2] = 2
dp[3] = 3

for i in range(4, N+1):
    dp[i] = dp[i-1] + 1

    for j in range(1, i+1):
        if j*j > i:
            break
        if dp[i] > dp[i - j*j] + 1:
            dp[i] = dp[i - j*j] + 1

print(dp[N])