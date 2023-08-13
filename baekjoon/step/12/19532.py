# ax + by = c
# dx + ey = f
# (a+d)x + (b+e)y = c+f
# 유일한 (x,y) 존재하며, x와 y는 정수

a, b, c, d, e, f = map(int, input().split())

for x in range(-999, 1000):
    isFind = False

    for y in range(-999, 1000):
        if a*x + b*y == c and d*x + e*y == f:
            isFind = True
            print(x, y)
            break

    if isFind:
        break