from collections import deque
import sys
input = sys.stdin.readline

EMPTY = '.'; WATER = '*'; STONE = 'X'; CAVE = 'D'; BEAVER = 'S'
FAIL = 'KAKTUS'

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

def get_board_info(row, col, board):
    waters = deque([])
    beaver = deque([])
    cave = (-1, -1)
    
    for r in range(row):
        for c in range(col):
            if board[r][c] == WATER:
                waters.append((r, c))
            elif board[r][c] == BEAVER:
                beaver.append((r, c))
            elif board[r][c] == CAVE:
                cave = (r, c)
    
    return waters, beaver, cave

def fill_water(waters, board):
    new_waters = []
    while waters:
        w_row, w_col = waters.popleft()

        for i in range(4):
            nr = dr[i] + w_row
            nc = dc[i] + w_col

            if 0 <= nr < row and 0 <= nc < col and board[nr][nc] != WATER and board[nr][nc] != STONE and board[nr][nc] != CAVE:
                board[nr][nc] = WATER
                new_waters.append((nr, nc))
    
    return new_waters

def move_beaver(beaver, board, cave, visited):
    new_beaver = []
    is_enter_cave = False

    while beaver:
        b_row, b_col = beaver.popleft()

        for i in range(4):
            nr = dr[i] + b_row
            nc = dc[i] + b_col

            if (nr, nc) == cave: is_enter_cave = True
            if 0 <= nr < row and 0 <= nc < col and not visited[nr][nc] and board[nr][nc] != STONE and board[nr][nc] != WATER:
                visited[nr][nc] = True
                new_beaver.append((nr, nc))
    
    return new_beaver, is_enter_cave

def enter_cave(waters, beaver, cave, board):
    visited = [[False] * col for _ in range(row)]
    visited[beaver[0][0]][beaver[0][1]] = True
    time = 0

    while True:
        time += 1

        # 1. 물 이동
        new_waters = fill_water(waters, board)

        # 2. 고슴도치 이동
        new_beaver, is_enter_cave = move_beaver(beaver, board, cave, visited)
        
        # 동굴에 도착했다면
        if is_enter_cave: return time

        # 더 이상 진행되는 것이 없다면
        if len(new_waters) == 0 and len(new_beaver) == 0:
            break

        # 초기화            
        waters = deque(new_waters)
        beaver = deque(new_beaver)

    return FAIL

row, col = map(int, input().split())
board = [list(input().strip()) for _ in range(row)]
    
waters, beaver, cave = get_board_info(row, col, board)
answer = enter_cave(waters, beaver, cave, board)

print(answer)