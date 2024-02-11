from collections import deque
import sys
sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

# 빙산에 있는 얼음을 구하는 함수
def get_ices_in_board():
    ices = deque([])

    for r in range(row):
        for c in range(col):
            if board[r][c] == 0: continue

            ices.append((r, c, board[r][c]))
    
    return ices

# 빙산을 녹이는 함수
def meltBoard():
    melt = []

    while ices:
        r, c, value = ices.popleft()
        cnt = 0

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < row and 0 <= nc < col and board[nr][nc] == 0:
                cnt += 1

        melt.append((r, c, value-cnt))

    for r, c, new_value in melt:
        board[r][c] = max(new_value, 0)

        if board[r][c] != 0:
            ices.append((r, c, board[r][c]))

def dfs(r, c, sid):
    global section
    section[r][c] = sid

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < row and 0 <= nc < col and board[nr][nc] != 0 and section[nr][nc] == 0:
            dfs(nr, nc, sid)

# 빙산이 두 덩어리 이상으로 분리되어 있는지 확인하는 함수
def isSeperateBoard():
    sid = 1

    for r, c, _ in ices:
        if board[r][c] == 0 or section[r][c] != 0: continue
        dfs(r, c, sid)
        sid += 1

    return True if sid > 2 else False

row, col = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(row)]
ices = get_ices_in_board()

time = 0
while ices:
    time += 1
    meltBoard()

    if not ices:
        time = 0
        break

    section = [[0] * col for _ in range(row)]
    if isSeperateBoard():
        break

print(time)