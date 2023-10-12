import sys
input = sys.stdin.readline

# ax + by = c
# dx + ey = f
a, b, c, d, e, f = map(int, input().split())

for x in range(-999, 1000):
    isFind = False

    for y in range(-999, 1000):
        if c == a*x + b*y and f == d*x + e*y:
            isFind = True
            print(x, y)
            break
    
    if isFind:
        break
