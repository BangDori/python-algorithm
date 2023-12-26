import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
chess_board = [list(input().rstrip()) for _ in range(N)]

boardB = [[0 for _ in range(M+1)] for _ in range(N+1)]
boardW = [[0 for _ in range(M+1)] for _ in range(N+1)]

for row in range(N):
    for col in range(M):
        if (row + col) % 2 == 0:
            if chess_board[row][col] == 'B':
                boardB[row][col] = 0 + boardB[row-1][col] + boardB[row][col-1] - boardB[row-1][col-1]
                boardW[row][col] = 1 + boardW[row-1][col] + boardW[row][col-1] - boardW[row-1][col-1]
            else:
                boardB[row][col] = 1 + boardB[row-1][col] + boardB[row][col-1] - boardB[row-1][col-1]
                boardW[row][col] = 0 + boardW[row-1][col] + boardW[row][col-1] - boardW[row-1][col-1]
        else:
            if chess_board[row][col] == 'B':
                boardB[row][col] = 1 + boardB[row-1][col] + boardB[row][col-1] - boardB[row-1][col-1]
                boardW[row][col] = 0 + boardW[row-1][col] + boardW[row][col-1] - boardW[row-1][col-1]
            else:
                boardB[row][col] = 0 + boardB[row-1][col] + boardB[row][col-1] - boardB[row-1][col-1]
                boardW[row][col] = 1 + boardW[row-1][col] + boardW[row][col-1] - boardW[row-1][col-1]

answer = sys.maxsize
for row in range(N-K+1):
    for col in range(M-K+1):
        subB = boardB[row+K-1][col+K-1] - boardB[row-1][col+K-1] - boardB[row+K-1][col-1] + boardB[row-1][col-1]
        subW = boardW[row+K-1][col+K-1] - boardW[row-1][col+K-1] - boardW[row+K-1][col-1] + boardW[row-1][col-1]

        answer = min(answer, subB, subW)

print(answer)