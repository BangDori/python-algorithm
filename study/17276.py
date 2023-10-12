import sys
input = sys.stdin.readline

# 역회전 (-45)
def rotate(X: list):
    size = len(X)
    
    depth = 0
    dir = 1
    max_depth = size // 2

    for depth in range(max_depth):
        row = depth
        col = depth
        temp = X[row][col]
        move = max_depth - depth

        for _ in range(2):
            X[row][col] = X[row][col + move*dir] 
            col += (move * dir)
        
        for _ in range(2):
            X[row][col] = X[row + move*dir][col]
            row += (move * dir)
        
        dir *= -1
        for _ in range(2):
            X[row][col] = X[row][col + move*dir]
            col += (move * dir)
        
        for _ in range(1):
            X[row][col] = X[row + move*dir][col]
            row += (move * dir)

        X[row][col] = temp

        dir *= -1

    return X

T = int(input())
X = [[] for _ in range(501)]

for _ in range(T):
    n, d = map(int, input().split())

    for i in range(n):
        X[i] = list(map(int, input().split()))
    
    d = (d//45 - 8) if d > 0 else (d//45)
    d = abs(d)
    
    if d == 0 or n == 1:
        rotated_X = X
    else:
        for _ in range(d):
            rotated_X = rotate(X[:n])

    for i in range(n):
        for j in range(n):
            print(rotated_X[i][j], end=' ')
        print()