from collections import deque
import sys
input = sys.stdin.readline

# 토끼의 현재 위치를 구한다
def get_rabbit_pos():
    for r in range(row):
        for c in range(col):
            if board[r][c] == RABBIT:
                return (r, c)

# dp를 통해 토끼가 이동할 수 있는 모든 경우의 수를 계산한다.
def get_max_carrot(rabbit_r, rabbit_c):
    # rabbit의 위치와 현재 당근의 수를 저장한다.
    carrot_board = [[-9999] * col for _ in range(row)]  # 당근의 수 저장
    max_carrot = -1

    carrot_board[rabbit_r][rabbit_c] = 0

    for c in range(col):
        for r in range(row):
            if board[r][c] == WALL: continue

            for dir in range(3):
                nr = r + dr[dir]
                nc = c + dc[dir]

                if 0 <= nr < row and 0 <= nc < col and board[nr][nc] != WALL:
                    if board[nr][nc] == CARROT:
                        carrot_board[nr][nc] = max(carrot_board[nr][nc], carrot_board[r][c] + 1)
                    elif board[nr][nc] == EMPTY:
                        carrot_board[nr][nc] = max(carrot_board[nr][nc], carrot_board[r][c])
                    elif board[nr][nc] == DOOR:
                        carrot_board[nr][nc] = max(carrot_board[nr][nc], carrot_board[r][c])
                        max_carrot = max(max_carrot, carrot_board[nr][nc])

    return max_carrot

WALL = '#'; CARROT = 'C'
DOOR = 'O'; RABBIT = 'R'
EMPTY = '.'

# 토끼는 →, ↘, ↗ 방향으로 이동
dr = [0, 1, -1]
dc = [1, 1, 1]

# 목표: 토끼가 최대한 많은 당근을 줍기
# 쪽문으로 나가야 하며, 토끼가 당근을 줍기 위해서는 그 당근이 있는 위치를 지나야 한다.
# 토끼가 어떤 쪽문에 도착했을때 반드시 그 문으로 탈출할 필요는 없으며, 더 움직여서 다른 쪽문으로 탈출해도 된다.

row, col = map(int, input().split())
board = [list(input().strip()) for _ in range(row)]

rabbit_r, rabbit_c = get_rabbit_pos()
answer = get_max_carrot(rabbit_r, rabbit_c)

print(answer)