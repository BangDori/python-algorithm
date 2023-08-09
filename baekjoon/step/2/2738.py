n, m = map(int, input().split())

matrixA = [[0 for _ in range(m)] for _ in range(n)]
matrixB = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    matrixA[i] = list(map(int, input().split()))

for i in range(n):
    matrixB[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(m):
        print(matrixA[i][j] + matrixB[i][j], end=' ')
    print()