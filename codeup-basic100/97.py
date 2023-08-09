h, w = map(int, input().split()) # 격자판의 세로, 가로
table = [[0 for _ in range(w+1)] for _ in range(h+1)]

n = int(input()) # 막대의 개수

for i in range(n):
    l, d, x, y = map(int, input().split()) # 막대의 길이, 방향, 좌표

    if d == 0: # 막대의 방향이 가로일 때
        for i in range(l):
            table[x][y+i] = 1
    else: # 막대의 방향이 세로일 때
        for i in range(l):
            table[x+i][y] = 1

for i in range(1, h+1):
    for j in range(1, w+1):
        print(table[i][j], end=' ')    
    print()
