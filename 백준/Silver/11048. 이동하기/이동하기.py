import sys
input = sys.stdin.readline

row, col = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(row)]
dp = [[0] * col for _ in range(row)]

dp[0][0] = maze[0][0]

for r in range(row):
    for c in range(col):
        if r-1 >= 0:
            dp[r][c] = max(dp[r][c], dp[r-1][c] + maze[r][c])
        if c-1 >= 0:
            dp[r][c] = max(dp[r][c], dp[r][c-1] + maze[r][c])
        if r-1 >= 0 and c-1 >= 0:
            dp[r][c] = max(dp[r][c], dp[r-1][c-1] + maze[r][c])

print(dp[-1][-1])