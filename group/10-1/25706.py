import sys
input = sys.stdin.readline

road_length = int(input())
jumps = list(map(int, input().split()))

dp = [0 for _ in range(road_length)]
dp[road_length-1] = 1

for idx in range(road_length-2, -1, -1):
    if jumps[idx] > 0:
        if idx+jumps[idx]+1 >= road_length:
            dp[idx] = 1
        else:
            dp[idx] = dp[idx+jumps[idx]+1] + 1
    else:
        dp[idx] = dp[idx+1] + 1

for idx in range(road_length):
    print(dp[idx], end=' ')