board = [[] for _ in range(19)]

for i in range(19):
    board[i] = list(map(int, input().split()))

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())

    for t in range(19):
        if board[x-1][t] == 1:
            board[x-1][t] = 0
        else:
            board[x-1][t] = 1
    
        if board[t][y-1] == 1:
            board[t][y-1] = 0
        else:
            board[t][y-1] = 1

for i in range(19):
    for j in range(19):
        print(board[i][j], end=' ')
    print()