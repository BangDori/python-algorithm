import sys
input = sys.stdin.readline

# 왼쪽 회전 -1
# 오른쪽 회전 +1

FORWARD = 'F'; BACK = 'B'
LEFT = 'L'; RIGHT = 'R'

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

TC = int(input())
for _ in range(TC):
    commands = list(input().strip())

    max_row = 0; min_row = 0
    max_col = 0; min_col = 0

    current = (0, 0, 0)
    for command in commands:
        row, col, dir = current

        if command == FORWARD:
            row += dr[dir]
            col += dc[dir]
        elif command == BACK:
            row += dr[(dir + 2) % 4]
            col += dc[(dir + 2) % 4]
        elif command == LEFT: dir = (dir-1) % 4
        elif command == RIGHT: dir = (dir+1) % 4

        current = (row, col, dir)
    
        max_row = max(max_row, row); min_row = min(min_row, row)
        max_col = max(max_col, col); min_col = min(min_col, col)

    print((max_row - min_row) * (max_col - min_col))