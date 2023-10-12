import sys
sys.setrecursionlimit(15000)
input = sys.stdin.readline

section = 0
def dfs(row, col):
    global section

    if matrix[row][col] != 0:
        return

    matrix[row][col] = 2
    section += 1
    if row-1 >= 0 and matrix[row-1][col] == 0:
        dfs(row-1, col)
    
    if row+1 <= matrix_row-1 and matrix[row+1][col] == 0:
        dfs(row+1, col)
    
    if col-1 >= 0 and matrix[row][col-1] == 0:
        dfs(row, col-1)

    if col+1 <= matrix_col-1 and matrix[row][col+1] == 0:
        dfs(row, col+1)

matrix_row, matrix_col, rect_count = map(int, input().split())
matrix = [[0 for _ in range(matrix_col)] for _ in range(matrix_row)]

for _ in range(rect_count):
    start_col, start_row, end_col, end_row  = map(int, input().split())

    end_col -= 1
    end_row -= 1

    for row in range(start_row, end_row+1):
        for col in range(start_col, end_col+1):
            matrix[row][col] = 1

answer = []
for row in range(matrix_row):
    for col in range(matrix_col):
        if matrix[row][col] != 0:
            continue
        
        dfs(row, col)
        answer.append(section)
        section = 0

answer.sort()

print(len(answer))
for ans in answer:
    print(ans, end=' ')