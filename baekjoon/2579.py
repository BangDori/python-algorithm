import sys
input = sys.stdin.readline

stair_count = int(input())
stairs = [0] + [int(input()) for _ in range(stair_count)]

dp = [[0] * 2 for _ in range(stair_count+1)]

dp[1][0] = stairs[1]

for i in range(2, stair_count+1):
    dp[i][0] = stairs[i] + max(dp[i-2][0], dp[i-2][1])
    dp[i][1] = stairs[i] + dp[i-1][0]

print(max(dp[-1][0], dp[-1][1]))