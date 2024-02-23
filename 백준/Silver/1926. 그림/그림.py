from collections import deque
import sys
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(current_r, current_c):
    count = 1
    queue = deque([(current_r, current_c)])

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c

            if 0 <= nr < row and 0 <= nc < col and not visited[nr][nc] and board[nr][nc] == 1:
                visited[nr][nc] = True
                queue.append((nr, nc))
                count += 1
    
    return count

row, col = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(row)]

sizes = []
visited = [[False] * col for _ in range(row)]

for r in range(row):
    for c in range(col):
        if board[r][c] == 0 or visited[r][c]: continue

        visited[r][c] = True
        picture = bfs(r, c)
        sizes.append(picture)

print(len(sizes))
print(max(sizes) if len(sizes) != 0 else 0)