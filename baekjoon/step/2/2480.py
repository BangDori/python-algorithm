x, y, z = map(int, input().split())
money = 0

if (x == y) & (y == z):
    money = 10000 + x * 1000
elif (x == y) | (y == z) | (z == x):
    if x == y: money = 1000 + x * 100
    elif y == z: money = 1000 + y * 100
    else: money = 1000 + z * 100
else:
    if x >= y:
        if x >= z:
            money = x * 100
        else:
            money = z * 100
    else:
        if y >= z:
            money = y * 100
        else:
            money = z * 100

print(money)