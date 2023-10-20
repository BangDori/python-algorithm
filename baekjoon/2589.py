# 육지(L) 바다(W)
# 상하좌우
# 한 칸 이동, 한시간

from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x_size, y_size = map(int, input().split())
island = [[] for _ in range(x_size)]

L_loc = []
for row in range(x_size):
    line = list(input().rstrip())

    for col in range(len(line)):
        if line[col] == 'L':
            L_loc.append((row, col))

    island[row] = line

timer = []
for i in range(len(L_loc)):
    visited = [[False] * y_size for _ in range(x_size)]
    queue = deque([L_loc[i]])

    time = 0
    while queue:
        time += 1

        for _ in range(len(queue)):
            x, y = queue.popleft()

            visited[x][y] = True

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if 0 <= nx < x_size and 0 <= ny < y_size and not visited[nx][ny]:
                    visited[nx][ny] = True
                    if island[nx][ny] == 'L':
                        queue.append((nx, ny))
    
    timer.append(time)
print(max(timer)-1)