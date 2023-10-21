# 자기보다 큰 물고기가 있는 칸은 지나갈 수 없음. 나머지는 가능
# 자신보다 작은 물고기만 먹을 수 있음.
# 크기가 동일하다면, 먹을 순 없지만, 이동은 가능

# 더 이상 먹을 수 있는 물고기가 없다면, 도움 요청
# 먹을 수 있는 물고기가 1마리라면, 그 물고기 먹으러 감
# 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기

# 거리는 지나야하는 칸의 개수의 최소값
# 거리가 가까운 물고기가 많다면, 가장 왼쪽에 있는 물고기

# 아기 상어 스스로 물고기를 잡아먹을 수 있는 시간을 출력

dx = [0, 1, -1, 0] # 상하
dy = [-1, 0, 0, 1] # 좌우

from collections import deque
import sys
input = sys.stdin.readline

size = int(input())
matrix = [[] for _ in range(size)]

# x, y, level
shark = (0, 0, 2)
shark_eat_count = 0
fishes = []

for row in range(size):
    line = list(map(int, input().split()))

    for col in range(len(line)):
        if line[col] == 9:
            shark = (row, col, 2)
        elif line[col] != 0:
            fishes.append((row, col, line[col]))

    matrix[row] = line

fishes.sort(key=lambda v: (v[0], v[1]))

def bfs(row, col):
    visited = [[False] * size for _ in range(size)]

    queue = deque([(shark[0], shark[1], shark[2], 0)])
    while queue:
        x, y, shark_level, dist = queue.popleft()
        visited[x][y] = True
        
        if x == row and y == col:
            return dist

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < size and 0 <= ny < size and not visited[nx][ny]:
                visited[nx][ny] = True
                if matrix[nx][ny] <= shark_level:
                    queue.append((nx, ny, shark_level, dist+1))

    return sys.maxsize

time = 0
while len(fishes) > 0:
    min_distance = sys.maxsize
    min_pos = (-1, -1, -1)

    for fish in fishes:
        row, col, fish_level = fish
        if fish_level >= shark[2]:
            continue

        distance = bfs(row, col)

        if distance < min_distance:
            min_distance = distance
            min_fish = fish
            
    if min_distance == sys.maxsize:
        break
    
    fishes.remove(min_fish)
    shark_eat_count += 1
    matrix[shark[0]][shark[1]] = 0
    if shark_eat_count == shark[2]:
        shark = (min_fish[0], min_fish[1], shark[2]+1)
        shark_eat_count = 0
    else:
        shark = (min_fish[0], min_fish[1], shark[2])
    matrix[shark[0]][shark[1]] = 9

    time += min_distance

print(time)