import sys
input = sys.stdin.readline

row, col = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(row)]

dp = [[0 for _ in range(col+1)] for _ in range(row+1)]
answer = 0

for x in range(1, row+1):
    for y in range(1, col+1):
        if matrix[x-1][y-1] == 0:
            dp[x][y] = min(dp[x-1][y-1], dp[x-1][y], dp[x][y-1]) + 1
            answer = max(answer, dp[x][y])

print(answer)