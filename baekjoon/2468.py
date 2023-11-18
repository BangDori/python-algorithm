from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

size = int(input())
city = [list(map(int, input().split())) for _ in range(size)]

distribution = {}

for row in city:
    for col in row:
        distribution[col] = 1

def dfs(row, col):
    section[row][col] = 2

    for i in range(4):
        nx = row + dx[i]
        ny = col + dy[i]

        if 0 <= nx < size and 0 <= ny < size and section[nx][ny] == 0:
            dfs(nx, ny)
    return

queue = deque(list(distribution.keys()))
queue.append(0)
answer = 0
while queue:
    rain_level = queue.popleft()

    # 0 초기, 1 침수, 2 안전영역
    area = deque([])
    section = [[0] * size for _ in range(size)]
    for row in range(size):
        for col in range(size):
            if city[row][col] <= rain_level:
                section[row][col] = 1
            else:
                area.append((row, col))

    safe_count = 0
    while area:
        row, col = area.popleft()

        if section[row][col] == 0:
            safe_count += 1

        dfs(row, col)
    
    answer = max(answer, safe_count)
print(answer)