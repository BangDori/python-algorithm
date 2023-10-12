while True:
    side = list(map(int, input().split()))

    side.sort(reverse=True)
    x, y, z = side

    if (x == 0) & (y == 0) & (z == 0):
        break

    if (y+z) <= x:
        print('Invalid')
        continue

    if x == y == z:
        print('Equilateral')
    elif (x == y) | (y == z) | (z == x):
        print('Isosceles')
    else:
        print('Scalene ')
