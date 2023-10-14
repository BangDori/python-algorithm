from collections import deque
import sys
input = sys.stdin.readline

x, y = map(int, input().split())
blocks = [list(map(int, input().split())) for _ in range(x)]

# 규칙 설정
d_count = int(input())
d = []
for _ in range(d_count):
    dx, dy = map(int, input().split())
    d.append((dx, dy))

# 초기 설정
queue = deque([])
for col in range(y):
    if blocks[0][col] == 1:
        queue.append((0, col))

time = 0
answer = -1
visited = [[False] * y for _ in range(x)]
while queue:
    size = len(queue)

    for _ in range(size):
        cur_x, cur_y = queue.popleft()

        if cur_x == x-1:
            answer = time
            queue.clear()
            break

        for move in d:
            dx, dy = move

            nx = cur_x + dx
            ny = cur_y + dy

            if 0 <= nx < x and 0 <= ny < y and not visited[nx][ny]:
                visited[nx][ny] = True

                if blocks[nx][ny] == 1:
                    queue.append((nx, ny))

    time += 1

print(answer)