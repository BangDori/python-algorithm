import sys
input = sys.stdin.readline

CROSS = '*'
EMPTY = '.'

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

row, col = map(int, input().split())
board = [list(input().strip()) for _ in range(row)]

def search_cross(row, col, board):
    cross = []

    for r in range(row):
        for c in range(col):
            if board[r][c] != CROSS: continue

            size = 1

            while True:
                count = 0
                for i in range(4):
                    nr = r + dr[i] * size
                    nc = c + dc[i] * size

                    if 0 <= nr < row and 0 <= nc < col:
                        if board[nr][nc] == CROSS:
                            count += 1
                
                if count == 4: 
                    cross.append((r, c, size))
                    size += 1
                else:
                    break
                
    return cross

def remove_cross(board, cross):
    for r, c, size in cross:

        board[r][c] = EMPTY
        for nr in range(r-size, r+size+1): board[nr][c] = EMPTY
        for nc in range(c-size, c+size+1):board[r][nc] = EMPTY

def is_valid_board(row, col, board):
    for r in range(row):
        for c in range(col):
            if board[r][c] == CROSS: return False
    
    return True

cross = search_cross(row, col, board)
remove_cross(board, cross)
is_valid = is_valid_board(row, col, board)

if is_valid:
    print(len(cross))
    for r, c, size in cross:
        print(r+1, c+1, size)
else:
    print(-1)