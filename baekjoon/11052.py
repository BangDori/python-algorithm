import sys
input = sys.stdin.readline

buy_card = int(input())
prices = [0] + list(map(int,input().split()))

dp = [0 for _ in range(buy_card+1)]

for idx in range(1, buy_card+1):
    for k in range(1, idx+1):
        dp[idx] = max(dp[idx], dp[idx-k] + prices[k])

print(dp[idx])