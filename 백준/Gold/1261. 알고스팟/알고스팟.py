from collections import deque
import sys
input = sys.stdin.readline

WALL = 1

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

col, row = map(int, input().split())
board = [list(map(int, list(input().strip()))) for _ in range(row)]
visited = [[1e9] * col for _ in range(row)]

# 현재 위치, 벽 부순 횟수
queue = deque([(0, 0, 0)])
visited[0][0] = 0

answer = 1e9
while queue:
    r, c, breakCount = queue.popleft()

    if r == row-1 and c == col-1:
        answer = min(answer, breakCount)
        continue

    if visited[r][c] < breakCount:
        continue

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < row and 0 <= nc < col:
            if board[nr][nc] == WALL and visited[nr][nc] > breakCount + 1:
                visited[nr][nc] = breakCount + 1
                queue.append((nr, nc, breakCount + 1))
            elif board[nr][nc] != WALL and visited[nr][nc] > breakCount:
                visited[nr][nc] = breakCount
                queue.append((nr, nc, breakCount))

print(answer)