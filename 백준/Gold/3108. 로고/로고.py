import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1,  0, -1]

def draw(x1, y1, x2, y2):
    for x in range(x1, x2+1):
        square[x][y1] = 1
        square[x][y2] = 1
    
    for y in range(y1, y2+1):
        square[x1][y] = 1
        square[x2][y] = 1

square_count = int(input())
square = [[0] * 2001 for _ in range(2001)]
stack = []
for _ in range(square_count):
    x1, y1, x2, y2 = map(int, input().split())
    x1 += 500; y1 += 500; x2 += 500; y2 += 500
    x1 *= 2; y1 *= 2; x2 *= 2; y2 *= 2
    draw(x1, y1, x2, y2)

    stack.append((x1, y1))

visited = [[False] * 2001 for _ in range(2001)]
PUcount = 0

def dfs(x, y, dir):
    if square[x][y] == 0:
        return
    
    visited[x][y] = True
    for k in range(4):
        nx = x + dx[(dir+k)%4]
        ny = y + dy[(dir+k)%4]

        if 0 <= nx < 2001 and 0 <= ny < 2001 and not visited[nx][ny] and square[nx][ny] == 1:
            dfs(nx, ny, (dir+k)%4)

answer = 0
for i in range(len(stack)):
    x, y = stack[i]
    if visited[x][y]:
        continue

    dfs(x, y, 0)
    answer += 1

print(answer if square[1000][1000] == 0 else answer-1)