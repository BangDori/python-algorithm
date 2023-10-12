import sys
input = sys.stdin.readline

def get_bingo_line(bingo):
    bingo_line = 0

    cross_bingo = 0
    reversed_cross_bingo = 0
    for row in range(5):
        row_bingo = 0
        col_bingo = 0

        for col in range(5):
            row_bingo = max(row_bingo, bingo[row][col])
            col_bingo = max(col_bingo, bingo[col][row])

        if row_bingo == 0:
            bingo_line += 1
        if col_bingo == 0:
            bingo_line += 1

        if row == 0:
            for x in range(5):
                cross_bingo = max(cross_bingo, bingo[x][x])
                reversed_cross_bingo = max(reversed_cross_bingo, bingo[4-x][x])

            if cross_bingo == 0:
                bingo_line += 1
            if reversed_cross_bingo == 0:
                bingo_line += 1

    return bingo_line

# 선이 3개 이상일 때 빙고
bingo = [list(map(int, input().split())) for _ in range(5)]
bingo_line = 3

call = [list(map(int, input().split())) for _ in range(5)]

def get_bingo(bingo):
    count = 0

    for c in call:
        for num in c:
            for i in range(5):
                for j in range(5):
                    if bingo[i][j] == num:
                        bingo[i][j] = 0
                        count += 1

                        if get_bingo_line(bingo) >= bingo_line:
                            answer = count
                            return answer

answer = get_bingo(bingo)
print(answer)