def getRePaintRect(board, pos_x, pos_y):
    B = "B"
    W = "W"
    b_count = 0
    w_count = 0

    for x in range(pos_x, pos_x+8):
        for y in range(pos_y, pos_y+8):
            if board[x][y] != B:
                b_count += 1
            
            if board[x][y] != W:
                w_count += 1

            tmp = B
            B = W
            W = tmp
                    
        tmp = B
        B = W
        W = tmp
    
    return b_count if b_count < w_count else w_count

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

pos_x = 0
pos_y = 0
answer = sys.maxsize

while pos_x + 8 <= N and pos_y + 8 <= M:
    count = getRePaintRect(board, pos_x, pos_y)
    if answer > count:
        answer = count

        if answer == 0:
            break

    pos_y += 1

    if pos_y + 8 > M:
        pos_x += 1
        pos_y = 0

print(answer)
