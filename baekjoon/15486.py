import sys
input = sys.stdin.readline

N = int(input())
times, prices = [0 for _ in range(N)], [0 for _ in range(N)]
for i in range(N):
    time, price = map(int, input().split())

    times[i] = time
    prices[i] = price

dp = [0 for _ in range(N)]
for i in range(N):
    dp[i] = max(dp[i], dp[i-1])
    next_time = times[i] + i - 1

    if next_time < N:
        dp[next_time] = max(dp[next_time], dp[i-1] + prices[i])

print(max(dp))