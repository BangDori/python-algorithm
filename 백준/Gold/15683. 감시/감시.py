import copy
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

EMPTY = 0; WALL = 6
MONITERED = -1

# 0 1 2 3
# 북 동 남 서
cctv_mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [0, 2, 3], [0, 1, 3]],
    [[0, 1, 2, 3]]
]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def get_cctv(board):
    cctv = []

    for r in range(row):
        for c in range(col):
            if board[r][c] == EMPTY or board[r][c] == WALL: continue

            cctv.append((r, c, board[r][c]))

    return cctv

def dfs(board, depth):
    global answer
    if depth == len(cctv):
        count = 0
        for line in board:
            count += line.count(0)
        answer = min(answer, count)
        return

    r, c, cid = cctv[depth]
    for mode in cctv_mode[cid]:
        copy_board = copy.deepcopy(board)
        monitor(copy_board, r, c, mode)
        dfs(copy_board, depth+1)

def monitor(board, r, c, mode):
    for dir in mode:
        nr = r
        nc = c

        while True:
            nr += dr[dir]
            nc += dc[dir]

            if 0 <= nr < row and 0 <= nc < col and board[nr][nc] != WALL:
                board[nr][nc] = MONITERED
            else:
                break

row, col = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(row)]
cctv = get_cctv(board)

answer = 64
dfs(board, 0)

print(answer)