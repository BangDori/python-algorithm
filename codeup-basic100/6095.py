board = [[0 for _ in range(20)] for _ in range(20)]
n = int(input())

for _ in range(n):
    x, y = map(int, input().split())

    board[x][y] = 1

for i in range(1, 20):
    for j in range(1, 20):
        print(board[i][j], end=' ')
    print()