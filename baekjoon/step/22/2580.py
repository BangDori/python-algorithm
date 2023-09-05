"""
    1. 가로, 세로줄에 1 ~ 9까지의 숫자
    2. 굵은 선으로 구분되어 있는 3x3 정사각형 안에 1 ~ 9 까지의 숫자
"""

import sys
input = sys.stdin.readline

isCompleted = 0

def check_sudoku(row, col, num):
    for i in range(9):
        if num == sudoku[row][i] and i != col:
            return False
        
        if num == sudoku[i][col] and i != row:
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

def show_sudoku():
    for i in range(9):
        for j in range(9):
            print(sudoku[i][j], end=' ')
        print()


def dfs(n):
    global isCompleted
    if n == len(search_list):
        isCompleted = True
        show_sudoku()
        return
    
    if isCompleted:
        return

    row, col = search_list[n]

    for num in range(1, 10):
        if check_sudoku(row, col, num): 
            sudoku[row][col] = num
            dfs(n+1)
            sudoku[row][col] = 0

sudoku = []
search_list = []
for row in range(9):
    col = list(map(int, input().split()))

    if col.count(0):
        for idx in range(len(col)):
            if col[idx] == 0:
                search_list.append((row, idx))

    sudoku += [col]

dfs(0)