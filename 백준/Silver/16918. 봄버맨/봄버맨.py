import sys
input = sys.stdin.readline

BOMB = 'O'
EMPTY = '.'
BOMB_TIME = 3

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

row, col, time = map(int, input().split())
board = [list(input().strip()) for _ in range(row)]
timer = [[0] * col for _ in range(row)]

def setupBomb(r, c, current_time):
    timer[r][c] = current_time + BOMB_TIME
    board[r][c] = BOMB

def aroundBoomBomb(r, c, current_time):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < row and 0 <= nc < col and timer[nr][nc] != current_time:
            currentBoomBomb(nr, nc)

def currentBoomBomb(r, c):
    board[r][c] = EMPTY
    timer[r][c] = 0

# 1. 폭탄 설정
for r in range(row):
    for c in range(col):
        if board[r][c] == BOMB:
            timer[r][c] = BOMB_TIME

# 2. 1초간 아무것도 하지 않음
current_time = 1

while current_time < time:
    # 3. 폭탄이 설치되지 있지 않은 모든 칸에 폭탄을 설치
    current_time += 1
    for r in range(row):
        for c in range(col):
            if timer[r][c] == 0: setupBomb(r, c, current_time)
    if current_time == time: break

    # 4. 3초 전에 설치된 폭탄이 모두 폭발한다.
    current_time += 1

    # 4-1. 주변 폭탄 우선 제거
    for r in range(row):
        for c in range(col):
            if timer[r][c] == current_time: aroundBoomBomb(r, c, current_time)

    # 4-2. 타이머가 만료된 현재 위치의 폭탄 제거
    for r in range(row):
        for c in range(col):
            if timer[r][c] == current_time: currentBoomBomb(r, c)

for r in range(row):
    for c in range(col):
        print(board[r][c], end='')
    print()