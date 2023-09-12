import sys
input = sys.stdin.readline

N = int(input())
dp = [1 for _ in range(N+1)]

for idx in range(2, N+1):
    dp[idx] = (dp[idx-1] + (dp[idx-2]*2)) % 10007
print(dp[N])