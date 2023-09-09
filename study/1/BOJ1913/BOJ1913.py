import sys
input = sys.stdin.readline

N = int(input())
find = int(input())
snail = [[0 for _ in range(N)] for _ in range(N)]

row = 0
col = 0
num = pow(N, 2)
dist = N # 이동 거리
dir = 1 # 방향
coord = -1, -1 # 찾은 좌표
while True:
    # row 이동
    for i in range(dist):
        snail[row + i*dir][col] = num
        num -= 1
    
    col += dir
    dist -= 1
    row += dist * dir

    if num == 0:
        break

    for i in range(dist):
        snail[row][col + i*dir] = num
        num -= 1
    col += (dist-1) * dir
    dir *= -1
    row += dir

for i in range(N):
    for j in range(N):
        if snail[i][j] == find:
            coord = i+1, j+1
        print(snail[i][j], end=' ')
    print()
print("%d %d" % (coord[0], coord[1]))