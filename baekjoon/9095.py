import sys
input = sys.stdin.readline

dp = [0, 1, 2, 4]

test_case = int(input())
for i in range(4, 12):
    next = dp[i-1] + dp[i-2] + dp[i-3]
    dp.append(next)

for _ in range(test_case):
    find = int(input())
    print(dp[find])