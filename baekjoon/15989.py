import sys
input = sys.stdin.readline

test_case = int(input().rstrip())

dp = [0, 1, 2, 3]

for _ in range(test_case):
    n = int(input().rstrip())

    if len(dp) <= n:
        for i in range(len(dp), n+1):
            dp.append(dp[i-3] + i//2 + 1)
    print(dp[n])