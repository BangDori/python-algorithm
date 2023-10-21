from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0] # 상하
dy = [0, 0, -1, 1] # 좌우

# x 세로, y 가로

test_case = int(input())

for _ in range(test_case):
    y, x, plant_count = map(int, input().split())
    matrix = [[0] * y for _ in range(x)]
    visited = [[False] * y for _ in range(x)]

    plant = deque([])

    for _ in range(plant_count):
        plant_y, plant_x = map(int, input().split())
        matrix[plant_x][plant_y] = 1

        plant.append((plant_x, plant_y))

    min_bug = 0
    while plant:
        queue = deque([plant.popleft()])

        while queue:
            cur_x, cur_y = queue.popleft()
            visited[cur_x][cur_y] = True

            for i in range(4):
                nx = cur_x + dx[i]
                ny = cur_y + dy[i]

                if 0 <= nx < x and 0 <= ny < y and not visited[nx][ny]:
                    visited[nx][ny] = True

                    if matrix[nx][ny] == 1:
                        matrix[nx][ny] = 0
                        plant.remove((nx, ny)); queue.append((nx, ny))

        min_bug += 1

    print(min_bug)