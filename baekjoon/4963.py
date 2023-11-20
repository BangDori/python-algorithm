from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

while True:
    size_y, size_x = map(int, input().split())

    if size_x == 0 and size_y == 0:
        break

    matrix = [list(map(int, input().split())) for _ in range(size_x)]

    land = deque([])
    for i in range(size_x):
        for j in range(size_y):
            if matrix[i][j] == 1:
                land.append((i, j))
    
    land_count = 0
    while land:
        x, y = land.popleft()

        if matrix[x][y] == 2:
            continue

        conn = deque([(x, y)])
        while conn:
            cur_x, cur_y = conn.popleft()
            for i in range(8):
                nx = cur_x + dx[i]
                ny = cur_y + dy[i]

                if 0 <= nx < size_x and 0 <= ny < size_y and matrix[nx][ny] == 1:
                    matrix[nx][ny] = 2
                    conn.append((nx, ny))
        
        land_count += 1
    print(land_count)