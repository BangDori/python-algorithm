import sys
input = sys.stdin.readline

# 가로, 세로, 대각선
N = int(input())
houses = [list(map(int, input().split())) for _ in range(N)]
answer = 0

def dfs(x, y, pipe):
    global answer
    if (x, y) == (N-1, N-1):
        answer += 1
        return

    # 0 가로
    if (pipe == 0 or pipe == 2) and y+1 < N:
        if houses[x][y+1] == 0:
            dfs(x, y+1, 0)
    
    # 1 세로
    if (pipe == 1 or pipe == 2) and x+1 < N:
        if houses[x+1][y] == 0:
            dfs(x+1, y, 1)

    # 2 대각선
    if x+1 < N and y+1 < N:
        if houses[x+1][y+1] == 0 and houses[x][y+1] == 0 and houses[x+1][y] == 0:
            dfs(x+1, y+1, 2)

dfs(0, 1, 0)
print(answer)