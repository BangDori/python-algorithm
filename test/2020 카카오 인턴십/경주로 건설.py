from collections import deque
import sys

   # 상(0) 하(1) 좌(2) 우(3)
dx = [1,    -1,   0,    0]
dy = [0,    0,   -1,    1]

def solution(board):
    size = len(board)
    answer = sys.maxsize
    
    cost = [[[sys.maxsize] * size for _ in range(size)] for _ in range(4)]
    # x, y, dir, money
    queue = deque([])
    
    cost[0][0][0] = 0
    if board[0][1] == 0:
        queue.append((0, 1, 3, 100))
        cost[3][0][1] = 100
    if board[1][0] == 0:
        queue.append((1, 0, 0, 100))
        cost[0][1][0] = 100
    
    while queue:
        x, y, dir, money = queue.popleft()
        
        if x == size-1 and y == size-1:
            answer = min(answer, money)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < size and 0 <= ny < size:
                if board[nx][ny] == 1:
                    continue

                if dir == i:
                    if cost[i][nx][ny] > money+100:
                        cost[i][nx][ny] = money+100

                        queue.append((nx, ny, i, money+100))
                else:
                    if cost[i][nx][ny] > money+600:
                        cost[i][nx][ny] = money+600
                        queue.append((nx, ny, i, money+600))
    
    return answer