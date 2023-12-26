import sys
input = sys.stdin.readline

line_count = int(input())
lines = []
for _ in range(line_count):
    src, dst = map(int, input().split())
    lines.append((src, dst))

lines.sort()

dp = [0] * line_count

for cur in range(line_count):
    increment_count = 1

    for prev in range(cur):
        if lines[prev][1] < lines[cur][1]:
            increment_count = max(increment_count, dp[prev]+1)
    
    dp[cur] = increment_count

print(line_count-max(dp))