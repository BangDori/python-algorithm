from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

sizeX, sizeY = map(int, input().split())
campus = [list(input().rstrip()) for _ in range(sizeX)]
visited = [[False] * sizeY for _ in range(sizeX)]

doyeon = (-1, -1)

for x in range(sizeX):
    for y in range(sizeY):
        if campus[x][y] == 'I':
            doyeon = (x, y)
            break
    
    if doyeon != (-1, -1):
        break

queue = deque([doyeon])
answer = 0
while queue:
    x, y = queue.popleft()

    if campus[x][y] == 'P':
        answer += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < sizeX and 0 <= ny < sizeY and not visited[nx][ny]:
            visited[nx][ny] = True

            if campus[nx][ny] != 'X':
                queue.append((nx, ny))

if answer == 0:
    print('TT')
else:
    print(answer)