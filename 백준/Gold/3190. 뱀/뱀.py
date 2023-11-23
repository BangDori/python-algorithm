# 0 right
# 1 down
# 2 left
# 3 up

from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

size = int(input().rstrip())
board = [[0] * size for _ in range(size)]
apple_count = int(input().rstrip())
for _ in range(apple_count):
    row, col = map(int, input().rstrip().split())
    board[row-1][col-1] = 2

L = int(input().rstrip())
conversation_info = deque([])
for _ in range(L):
    sec, dir = input().rstrip().split()
    conversation_info.append((int(sec), dir))

queue = deque([(0, 0)])
x, y = 0, 0
time = 0
dir = 0

board[x][y] = 1

while queue:
    if conversation_info and time == conversation_info[0][0]:
        sec, conversation = conversation_info.popleft()

        if conversation == 'D':
            dir = (dir + 1) % 4
        if conversation == 'L':
            dir = (dir - 1) % 4
    
    x += dx[dir]
    y += dy[dir]

    if not (0 <= x < size and 0 <= y < size):
        break

    if board[x][y] == 2:
        board[x][y] = 1
        queue.append((x, y))
        time += 1

    elif board[x][y] == 0:
        board[x][y] = 1
        queue.append((x, y))
        tail_x, tail_y = queue.popleft()
        board[tail_x][tail_y] = 0
        time += 1
    else:
        break
    
print(time+1)