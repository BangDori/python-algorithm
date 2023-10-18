from collections import deque
import sys
input = sys.stdin.readline

d = [
  (-1, -2),
  (-2, -1),
  (-2, 1),
  (-1, 2),
  (1, 2),
  (2, 1),
  (2, -1),
  (1, -2)
]

room_size, bug_count, clean_count, after_day = map(int, input().split())
room = [[0] * room_size for _ in range(room_size)]

queue = deque([])
visited = [[[False]*2 for _ in range(room_size)] for _ in range(room_size)]
for _ in range(bug_count):
    x, y = map(int, input().split())

    room[x-1][y-1] = 1
    queue.append((x-1,y-1,0))
    visited[x-1][y-1][0] = True

cleans = []
for _ in range(clean_count):
    x, y = map(int, input().split())
    cleans.append((x-1, y-1))

cur_day = 0
while queue and cur_day < after_day:
    queue_size = len(queue)

    for _ in range(queue_size):
        x, y, day = queue.popleft()
        room[x][y] = 0

        isVirus = False
        for dx, dy in d:
            nx = x + dx
            ny = y + dy

            next_day = (day+1) % 2

            if 0 <= nx < room_size and 0 <= ny < room_size and not visited[nx][ny][next_day]:
                visited[nx][ny][next_day] = True
                queue.append((nx, ny, day+1))
                isVirus=True

        if not isVirus:
            visited[x][y][(day%2)]=False
    cur_day += 1

check_day = after_day % 2
for cx, cy in cleans:
    if visited[cx][cy][check_day]:
        print("YES")
        exit(0)

print("NO")