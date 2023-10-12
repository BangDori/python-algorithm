def GCD(a, b):
    min_num = min(a, b)
    max_num = max(a, b)

    gcd = 1
    while True:
        tmp = max_num % min_num

        if tmp == 0:
            gcd = min_num
            break

        max_num = min_num
        min_num = tmp
    
    return gcd


x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

x = (x1 * y2) + (x2 * y1)
y = y1 * y2
gcd = GCD(x, y)

print(int(x/gcd), int(y/gcd))