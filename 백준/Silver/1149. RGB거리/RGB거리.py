import sys
input = sys.stdin.readline

N = int(input())
houses = [list(map(int, input().split())) for _ in range(N)]

dp = [[sys.maxsize] * 3 for _ in range(N)]
dp[0] = houses[0]

for i in range(1, N):
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            
            dp[i][k] = min(dp[i][k], dp[i-1][j] + houses[i][k])

print(min(dp[-1]))