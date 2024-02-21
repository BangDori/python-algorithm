import sys
input = sys.stdin.readline

GROUND = 'X'; WATER = '.'

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

row, col = map(int, input().split())
map = [list(input().strip()) for _ in range(row)]

stack = []

for r in range(row):
    for c in range(col):
        if map[r][c] == WATER: continue

        count = 0

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < row and 0 <= nc < col:
                if map[nr][nc] == WATER: count += 1
            else:
                count += 1
        
        stack.append((r, c, count))

min_row = row-1; max_row = 0
min_col = col-1; max_col = 0

while stack:
    r, c, count = stack.pop()

    if count >= 3: map[r][c] = WATER
    else:
        min_row = min(min_row, r); max_row = max(max_row, r)
        min_col = min(min_col, c); max_col = max(max_col, c)

for r in range(min_row, max_row+1):
    for c in range(min_col, max_col+1):
        print(map[r][c], end='')
    print()