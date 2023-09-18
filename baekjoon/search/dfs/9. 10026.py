import sys
sys.setrecursionlimit(15000)
input = sys.stdin.readline

def dfs(row, col, matrix, color):
    if color.find(matrix[row][col]) == -1:
        return

    matrix[row][col] = 'X'

    if col-1 >= 0 and color.find(matrix[row][col-1]) != -1:
        dfs(row, col-1, matrix, color)
    
    if col+1 <= size-1 and color.find(matrix[row][col+1]) != -1:
        dfs(row, col+1, matrix, color)

    if row-1 >= 0 and color.find(matrix[row-1][col]) != -1:
        dfs(row-1, col, matrix, color)

    if row+1 <= size-1 and color.find(matrix[row+1][col]) != -1:
        dfs(row+1, col, matrix, color)

size = int(input())
RGB = [list(input()) for _ in range(size)]
RGB_copy = [[RGB[i][j] for j in range(size)] for i in range(size)]

answer1 = 0
for row in range(size):
    for col in range(size):
        if RGB[row][col] == 'X':
            continue
        
        answer1 += 1
        dfs(row, col, RGB, RGB[row][col])

answer2 = 0
for row in range(size):
    for col in range(size):
        if RGB_copy[row][col] == 'X':
            continue
        
        answer2 += 1
        if RGB_copy[row][col] == 'R' or RGB_copy[row][col] == 'G':
            dfs(row, col, RGB_copy, 'RG')
        else:
            dfs(row, col, RGB_copy, 'B')

print(answer1, answer2)