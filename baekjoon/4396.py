import sys
input = sys.stdin.readline

def get_mine_count(row, col):
    mine_count = 0

    for r in range(row-1, row+2):
        if r < 0 or r > size-1:
            continue

        for c in range(col-1, col+2):
            if c < 0 or c > size-1:
                continue

            if mine[r][c] == '*':
                mine_count += 1

    # 8방향 분석
    return mine_count


size = int(input())
mine = [list(input().rstrip()) for _ in range(size)]
play = [list(input().rstrip()) for _ in range(size)]

mine_loc = []
isLose = False

for row in range(size):
    for col in range(size):
        if mine[row][col] == '*':
            mine_loc.append((row, col))

        if play[row][col] == '.':
            continue

        if mine[row][col] == '*':
            isLose = True


        play[row][col] = get_mine_count(row, col)

if isLose:
    for row, col in mine_loc:
        play[row][col] = '*'

for row in range(size):
    for col in range(size):
        print(play[row][col], end='')
    print()