import sys
sys.setrecursionlimit(250 * 250)
input = sys.stdin.readline

DOT = '.'; FENCE = '#'
SHEEP = 'o'; WOLF = 'v'

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

def search_section(r, c, sid, section):
    tot_sheep, tot_wolf = 0, 0
    if board[r][c] == SHEEP: tot_sheep += 1
    elif board[r][c] == WOLF: tot_wolf += 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < row and 0 <= nc < col and section[nr][nc] == 0:
            section[nr][nc] = sid
            sheep, wolf = search_section(nr, nc, sid, section)

            tot_sheep += sheep; tot_wolf += wolf

    return tot_sheep, tot_wolf

def compare_section(row, col, board):
    total_sheep, total_wolf = 0, 0
    section = [[0 if board[r][c] != FENCE else -1 for c in range(col)] for r in range(row)]
    sid = 1

    for r in range(row):
        for c in range(col):
            if board[r][c] == FENCE or section[r][c] != 0: continue

            section[r][c] = sid
            sheep, wolf = search_section(r, c, sid, section)

            if sheep > wolf: total_sheep += sheep
            else: total_wolf += wolf

            sid += 1
    
    return total_sheep, total_wolf

# 입력
row, col = map(int, input().split())
board = [list(input().strip()) for _ in range(row)]
sheep, wolf = compare_section(row, col, board)

print(sheep, wolf)