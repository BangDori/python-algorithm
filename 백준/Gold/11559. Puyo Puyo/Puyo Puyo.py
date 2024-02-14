import sys
input = sys.stdin.readline

ROW = 12
COL = 6
EMPTY = '.'
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, color, li):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < ROW and 0 <= nc < COL and not visited[nr][nc] and field[nr][nc] == color:
            visited[nr][nc] = True
            li.append((nr, nc))
            dfs(nr, nc, color, li)

def puyo_puyo():
    global is_puyo
    for r in range(ROW):
        for c in range(COL):
            if visited[r][c] or field[r][c] == EMPTY: continue

            visited[r][c] = True
            color_li = [(r, c)]
            dfs(r, c, field[r][c], color_li)
            
            if len(color_li) >= 4:
                is_puyo = True
                for pr, pc in color_li:
                    field[pr][pc] = EMPTY

def down_puyo():
    for r in range(ROW-1, -1, -1):
        for c in range(COL):
            if field[r][c] != EMPTY: continue

            for r2 in range(r-1, -1, -1):
                if field[r2][c] != EMPTY:
                    field[r][c] = field[r2][c]
                    field[r2][c] = EMPTY
                    break

field = [list(input().strip()) for _ in range(ROW)]

chain = 0
while True:
    is_puyo = False
    visited = [[False] * COL for _ in range(ROW)]

    puyo_puyo()
    if not is_puyo: break

    chain += 1
    down_puyo()

print(chain)