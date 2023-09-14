import sys
input = sys.stdin.readline

# 뒤집기
def reverse_matrix(row, col):
    for r in range(row, row+3):
        for c in range(col, col+3):
            if matrixA[r][c] == 0:
                matrixA[r][c] = 1
            else:
                matrixA[r][c] = 0

row, col = map(int, input().split())
matrixA = [list(map(int, input().rstrip())) for _ in range(row)]
matrixB = [list(map(int, input().rstrip())) for _ in range(row)]

answer = 0
if (row < 3 or col < 3) and matrixA != matrixB:
    answer = -1
else:
    for r in range(row-2):
        for c in range(col-2):
            if matrixA[r][c] != matrixB[r][c]:
                answer += 1
                reverse_matrix(r, c)

    if matrixA != matrixB:
        answer = -1

print(answer)