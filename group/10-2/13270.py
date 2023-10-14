import sys
input = sys.stdin.readline

# 0: min, 1: max
dp=[[0, 0, 1, 2, 2, 3] for _ in range(2)]

N = int(input())

if N <= 5:
    print(dp[0][N], dp[1][N])
else:
    for idx in range(6, N+1):
        next_min = dp[0][idx-1]+1
        next_max = dp[1][idx-1]

        for jdx in range(2, idx-1):
            next_min = min(next_min, dp[0][jdx]+dp[0][idx-jdx])
            next_max = max(next_max, dp[1][jdx]+dp[1][idx-jdx])
        
        dp[0].append(next_min)
        dp[1].append(next_max)

    print(dp[0][N], dp[1][N])