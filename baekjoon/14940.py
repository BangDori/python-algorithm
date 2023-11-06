from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

rows, cols = map(int, input().split())
matrix = [[] for _ in range(rows)]

start = -1

for row in range(rows):
    line = list(map(int, input().split()))

    if start == -1:
        for col in range(len(line)):
            if line[col] == 2:
                start = (row, col, 0)
                break
    
    matrix[row] = line

queue = deque([start])
dist = [[matrix[x][y] for y in range(cols)] for x in range(rows)]
visited = [[False]*cols for _ in range(rows)]
dist[start[0]][start[1]] = start[2]
visited[start[0]][start[1]] = True

while queue:
    x, y, move = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
            visited[nx][ny] = True
            if matrix[nx][ny] == 0:
                continue

            dist[nx][ny] = move+1
            queue.append((nx, ny, move+1))

for x in range(rows):
    for y in range(cols):
        if matrix[x][y] == 0:
            print(0, end=' ')
        elif not visited[x][y]:
            print(-1, end=' ')
        else:
            print(dist[x][y], end=' ')
    print()