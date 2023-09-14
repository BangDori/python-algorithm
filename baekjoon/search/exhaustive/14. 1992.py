import sys
input = sys.stdin.readline

n = int(input())
video = [list(map(int, input().rstrip())) for _ in range(n)]

def dfs(x, y, n):
    check = video[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != video[i][j]:
                check = -1
                break
    
    if check == -1:
        n //= 2
        print('(', end='')
        dfs(x, y, n)
        dfs(x, y+n, n)
        dfs(x+n, y, n)
        dfs(x+n, y+n, n)
        print(')', end='')
    else:
        print(check, end='')

dfs(0, 0, n)