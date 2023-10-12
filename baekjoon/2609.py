def getGCD(n, m):
    max_num = max(n, m)
    min_num = min(n, m)

    gcd = 1
    while True:
        r = max_num % min_num

        if r == 0:
            gcd = min_num
            break

        max_num = min_num
        min_num = r

    return gcd

n, m = map(int, input().split())
gcd = getGCD(n, m)

print(gcd)
print(int((n/gcd)*(m/gcd)*gcd))