import sys
input = sys.stdin.readline

N = int(input())
min_dp = [[0 for _ in range(3)] for _ in range(2)]
max_dp =[[0 for _ in range(3)] for _ in range(2)]

for _ in range(N):
    a, b, c = map(int, input().split())

    max_dp[1][0] = max(max_dp[0][0]+a, max_dp[0][1]+a)
    max_dp[1][1] = max(max_dp[0][0]+b, max_dp[0][1]+b, max_dp[0][2]+b)
    max_dp[1][2] = max(max_dp[0][1]+c, max_dp[0][2]+c)

    max_dp[0][0] = max_dp[1][0]; max_dp[0][1] = max_dp[1][1]; max_dp[0][2] = max_dp[1][2]

    min_dp[1][0] = min(min_dp[0][0]+a, min_dp[0][1]+a)
    min_dp[1][1] = min(min_dp[0][0]+b, min_dp[0][1]+b, min_dp[0][2]+b)
    min_dp[1][2] = min(min_dp[0][1]+c, min_dp[0][2]+c)

    min_dp[0][0] = min_dp[1][0]; min_dp[0][1] = min_dp[1][1]; min_dp[0][2] = min_dp[1][2]

print(max(max_dp[-1]), min(min_dp[-1]))