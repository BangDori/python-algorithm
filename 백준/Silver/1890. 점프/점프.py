import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

dp[0][0] = 1

for row in range(N):
    for col in range(N):
        if dp[row][col] == 0 or (row, col) == (N-1, N-1): continue

        # ↓
        if row + board[row][col] < N:
            dp[row + board[row][col]][col] += dp[row][col]
        
        # →
        if col + board[row][col] < N:
            dp[row][col + board[row][col]] += dp[row][col]

print(dp[-1][-1])