import sys
input = sys.stdin.readline

N = int(input())
drinks = [int(input()) for _ in range(N)]

if N == 1:
    print(drinks[-1])
elif N == 2:
    print(sum(drinks))
else:
    dp = [0 for _ in range(N)]
    dp[0] = drinks[0]
    dp[1] = dp[0] + drinks[1]
    dp[2] = max(dp[0] + drinks[2], drinks[1] + drinks[2], dp[1])

    for i in range(3, N):
        dp[i] = max(dp[i-2] + drinks[i], dp[i-3] + drinks[i-1] + drinks[i], dp[i-1])

    print(dp[-1])