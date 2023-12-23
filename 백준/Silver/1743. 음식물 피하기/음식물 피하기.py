import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

row, col, trash_count = map(int, input().split())
matrix = [[0] * col for _ in range(row)]

trashs = []
for _ in range(trash_count):
    r, c = map(int, input().split())
    r -= 1; c -= 1

    trashs.append((r, c))
    matrix[r][c] = -1

def dfs(r, c):
    global count

    if visited[r][c]:
        return
    visited[r][c] = True
    count += 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < row and 0 <= nc < col:
            if matrix[nr][nc] == -1:
                dfs(nr, nc)

visited = [[False] * col for _ in range(row)]
answer = 0
for r, c in trashs:
    if not visited[r][c]:
        count = 0
        dfs(r, c)

        answer = max(answer, count)

print(answer)