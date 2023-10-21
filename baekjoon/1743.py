from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

x, y, trash_count = map(int, input().split())
matrix = [[0] * y for _ in range(x)]
visited = [[False] * y for _ in range(x)]
trash = deque([])

for _ in range(trash_count):
    trash_x, trash_y = map(int, input().split())
    trash_x -= 1
    trash_y -= 1

    matrix[trash_x][trash_y] = 1
    trash.append((trash_x, trash_y))

max_size = 0
while trash:
    trash_x, trash_y = trash.pop()
    visited[trash_x][trash_y] = True

    queue = deque([(trash_x, trash_y)])
    size = 1
    while queue:
        cur_x, cur_y = queue.popleft()

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if 0 <= nx < x and 0 <= ny < y and not visited[nx][ny]:
                visited[nx][ny] = True

                if matrix[nx][ny] == 1:
                    trash.remove((nx, ny))
                    queue.append((nx, ny))
                    size += 1

    if size > max_size:
        max_size = size
print(max_size)