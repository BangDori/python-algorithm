t = [[0 for _ in range(20)] for _ in range(20)]

for i in range(1, 20):
    t[i] = input().split()
    t[i].insert(0, 0)

c = int(input())

for i in range(c):
    x, y = input().split()

    x = int(x)
    y = int(y)

    for j in range(1, 20):
        if int(t[j][y]) == 0:
            t[j][y] = 1
        else:
            t[j][y] = 0
        
        if int(t[x][j]) == 0:
            t[x][j] = 1
        else:
            t[x][j] = 0

for i in range(1, 20):
    for j in range(1, 20):
        print(t[i][j], end=' ')
    
    print()
