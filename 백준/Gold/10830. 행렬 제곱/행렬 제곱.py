import sys
input = sys.stdin.readline

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

def mul_matrix(mtrx1, mtrx2):
    new_matrix = [[0]*N for _ in range(N)] 
    for i in range(N):
        for j in range(N):
            for k in range(N):
                new_matrix[i][j] += mtrx1[i][k] * mtrx2[k][j] % 1000

    return new_matrix

def divide_and_conquer(A, count):
    if count == 1:
        return A
    else:
        new_matrix = divide_and_conquer(A, count // 2)

        if count % 2 == 0:
            return mul_matrix(new_matrix, new_matrix)
        else:
            return mul_matrix(mul_matrix(new_matrix, new_matrix), A)

answer = divide_and_conquer(A, B)

for row in answer:
    for col in row:
        print(col % 1000, end=' ')
    print()