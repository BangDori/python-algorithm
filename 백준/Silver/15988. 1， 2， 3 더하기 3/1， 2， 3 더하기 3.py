import sys
input = sys.stdin.readline

MOD = 1000000009

TC = int(input())
tests = [int(input()) for _ in range(TC)]

max_test = max(tests)
dp = [0 for _ in range(max_test + 1)]
dp[1] = 1; dp[2] = 2; dp[3] = 4

for i in range(4, max_test+1):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % MOD

for test in tests:
    print(dp[test])