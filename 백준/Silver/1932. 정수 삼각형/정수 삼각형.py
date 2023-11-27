import sys
input = sys.stdin.readline

size = int(input())
triangle = []
for _ in range(size):
    line = list(map(int, input().split()))
    triangle += line

lines = [0]
for i in range(1, len(triangle)):
    if len(triangle) < lines[-1]:
        break
    lines.append(lines[-1] + i)

dp = [0 for _ in range(len(triangle))]
dp[0] = triangle[0]

for i in range(len(triangle)-size):
    next = 0
    for k, line in enumerate(lines):
        if i < line:
            next = k
            break
        
    dp[i+next] = max(dp[i+next], dp[i] + triangle[i+next])
    dp[i+next+1] = max(dp[i+next+1], dp[i] + triangle[i+next+1])

print(max(dp))