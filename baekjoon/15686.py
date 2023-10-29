from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

size, select_count = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(size)]

chicken_house = []

for row in range(size):
    for col in range(size):
        if table[row][col] == 2:
            chicken_house.append((row, col))

def dfs(chicken_queue):
    queue = deque(chicken_queue)
    visited = [[False] * size for _ in range(size)]

    total_distance = 0
    while queue:
        chicken_x, chicken_y, distance = queue.popleft()

        if table[chicken_x][chicken_y] == 1:
            total_distance += distance

        for i in range(4):
            nx = chicken_x + dx[i]
            ny = chicken_y + dy[i]

            if 0 <= nx < size and 0 <= ny < size and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, distance+1))

    return total_distance

answer = sys.maxsize
for select_chicken in combinations(chicken_house, select_count):
    chicken_queue = []

    for chicken_x, chicken_y in select_chicken:
        chicken_queue.append((chicken_x, chicken_y, 0))
    distance = dfs(chicken_queue)

    if distance < answer:
        answer = distance
print(answer)