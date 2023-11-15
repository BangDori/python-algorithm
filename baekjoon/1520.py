import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

row, col = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(row)]

dp = [[-1 for _ in range(col)] for _ in range(row)]
answer = 0

def dfs(x, y):
    if x == row-1 and y == col-1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    dp[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < row and 0 <= ny < col and matrix[nx][ny] < matrix[x][y]:
            dp[x][y] += dfs(nx, ny)
    
    return dp[x][y]

answer = dfs(0, 0)
print(answer)