import sys
input = sys.stdin.readline

N = int(input())
periods = []; costs = []

for _ in range(N):
    period, cost = map(int, input().split())
    periods.append(period), costs.append(cost)

dp = [0 for _ in range(N)]

for today in range(N):
    max_cost = costs[today] if today + periods[today] <= N else 0

    if max_cost != 0:
        for prev in range(today):
            if prev+periods[prev] <= today:
                max_cost = max(max_cost, costs[today] + dp[prev])
    
    dp[today] = max_cost

print(max(dp))