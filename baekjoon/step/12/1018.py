def getRePaintCount(board, start):
    rePaint = 0
    current = start
    next = 'B' if start == 'W' else 'W'
    
    # print(current, next)
    for i in range(8):
        for j in range(8):
            if current != board[i][j]:
                board[i][j] = current
                rePaint += 1
            
            temp = current
            current = next
            next = temp
        
        if i == 7:
            break
       
        current = 'B' if board[i][0] == 'W' else 'W'
        next = 'B' if current == 'W' else 'W'

    return rePaint


# board의 높이 (n), 너비 (m)
n, m = map(int, input().split())
board = [[0 for _ in range(m)] for _ in range(n)]
check_board = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    board[i] = list(input())

pos_x = 0
pos_y = 0

min = 99999
while (pos_x + 8 <= n) & (pos_y + 8 <= m):
    slice_board = [[board[i][j] for j in range(pos_y, pos_y+8)] for i in range(pos_x, pos_x+8)]
    slice_board2 = [[board[i][j] for j in range(pos_y, pos_y+8)] for i in range(pos_x, pos_x+8)]
    
    rePaintFirst = getRePaintCount(slice_board, 'B')
    rePaintSecond = getRePaintCount(slice_board2, 'W')

    if rePaintFirst > rePaintSecond:
        if min > rePaintSecond:
            min = rePaintSecond
    else:
        if min > rePaintFirst:
            min = rePaintFirst

    pos_y += 1

    if pos_y + 7 == m:
        pos_y = 0
        pos_x += 1

print(min)