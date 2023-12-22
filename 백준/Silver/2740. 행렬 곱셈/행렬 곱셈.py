import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrixA = [list(map(int, input().split())) for _ in range(N)]

M, K = map(int, input().split())
matrixB = [list(map(int, input().split())) for _ in range(M)]

# matrixA * matrixB

matrixC = [[0] * K for _ in range(N)]

for k in range(M):
    for x in range(N):
        for y in range(K):
            matrixC[x][y] += matrixA[x][k] * matrixB[k][y]

for x in range(N):
    for y in range(K):
        print(matrixC[x][y], end=' ')
    print()