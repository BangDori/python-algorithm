import sys
sys.setrecursionlimit(10 ** 2)
input = sys.stdin.readline

SIZE = 9
sudoku = [list(map(int, input().strip())) for _ in range(SIZE)]

def get_blank(sudoku):
    blank = []

    for row in range(SIZE):
        for col in range(SIZE):
            if sudoku[row][col] == 0:
                blank.append((row, col))
    
    return blank

def is_valid_num(row, col, num):
    for i in range(SIZE):
        if sudoku[i][col] == num and i != row:
            return False

        if sudoku[row][i] == num and i != col:
            return False
        
    row3 = row // 3
    col3 = col // 3

    for r in range(row3*3, row3*3+3):
        for c in range(col3*3, col3*3+3):
            if row == r and col == c:
                continue

            if num == sudoku[r][c]:
                return False
    
    return True

def back_tracking(cnt):
    if cnt >= len(blank):
        for r in range(SIZE):
            for c in range(SIZE):
                print(sudoku[r][c], end='')
            print()
        exit(0)

    row, col = blank[cnt]
    for num in range(1, 10):
        if is_valid_num(row, col, num):
            sudoku[row][col] = num
            back_tracking(cnt+1)
        sudoku[row][col] = 0

    return

blank = get_blank(sudoku)
back_tracking(0)