import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def check_top(r, c):
    global is_top

    visited[r][c] = True

    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < row and 0 <= nc < col:
            if farm[nr][nc] > farm[r][c]:
                is_top = False
            elif not visited[nr][nc] and farm[nr][nc] == farm[r][c]:
                check_top(nr, nc)

dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]

row, col = map(int, input().split())
farm = [list(map(int, input().split())) for _ in range(row)]
visited = [[False for _ in range(col)] for _ in range(row)]

top = 0

for r in range(row):
    for c in range(col):
        if visited[r][c]:
            continue

        is_top = True
        check_top(r, c)
        if is_top: top += 1

print(top)