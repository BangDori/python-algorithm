import sys
input = sys.stdin.readline

test_case = int(input())

dp = [0 for _ in range(101)]
dp[1] = dp[2] = dp[3] = 1
dp[4] = dp[5] = 2

for i in range(6, len(dp)):
    dp[i] = dp[i-5] + dp[i-1]

for _ in range(test_case):
    N = int(input())
    print(dp[N])