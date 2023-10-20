from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x_size, y_size = map(int, input().split())
robot = tuple(map(int, input().split()))
matrix = [list(map(int, input().split())) for _ in range(x_size)]

answer = 0

queue = deque([robot])
while queue:
    x, y, dir = queue.popleft()

    # 현재 칸 청소
    if matrix[x][y] == 0:
        matrix[x][y] = 2
        answer += 1

    # 주변 4칸 검사
    isMove = False
    for i in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        dir = (dir+3)%4

        if 0 <= nx < x_size and 0 <= ny < y_size:
            # 청소되지 않은 빈 칸이 있는 경우
            if matrix[nx][ny] == 0:
                isMove = True

    if isMove:
        dir = (dir+3)%4
        nx = x + dx[dir]
        ny = y + dy[dir]
        
        if 0 <= nx < x_size and 0 <= ny < y_size and matrix[nx][ny] == 0:
            queue.append((nx, ny, dir))
        else:
            queue.append((x, y, dir))

    # 4칸 중 청소되지 않은 칸이 없는 경우
    if not isMove:
        # 후진
        nx = x + dx[(dir+2)%4]
        ny = y + dy[(dir+2)%4]

        if 0 <= nx < x_size and 0 <= ny < y_size:
            # 바라보는 방향을 유지한 채로 한 칸 후진
            if matrix[nx][ny] != 1:
                queue.append((nx, ny, dir))
        else:
            break

print(answer)