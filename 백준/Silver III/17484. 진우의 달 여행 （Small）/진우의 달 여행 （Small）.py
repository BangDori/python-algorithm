import sys
sys.setrecursionlimit(10 ** 2)
input = sys.stdin.readline

dc = [-1, 0, 1]

row, col = map(int,input().split())
table = [list(map(int,input().split())) for _ in range(row)]

answer = 1e9

def dfs(r, c, dir, tot):
    global answer
    if r+1 == row:
        answer = min(answer, tot)
        return
    
    for next in range(3):
        if next == dir: continue

        nc = dc[next] + c
        if 0 <= nc < col:
            dfs(r+1, nc, next, tot + table[r+1][nc])

for c in range(col):
    dfs(0, c, -1, table[0][c])
print(answer)