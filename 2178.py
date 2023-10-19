from collections import deque
import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

x, y = map(int, input().split())
maze = [list(input()) for _ in range(x)]
visited = [[False]*y for _ in range(x)]

queue = deque([(0, 0, 1)])

while queue:
    cur_x, cur_y, count = queue.popleft()

    if cur_x == x-1 and cur_y == y-1:
        print(count)
        break

    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]

        if 0 <= nx < x and 0 <= ny < y and not visited[nx][ny]:
            visited[nx][ny] = True
            if maze[nx][ny] == '1':
                queue.append((nx, ny, count+1))