def getGCD(a, b):
    min_num = min(a, b)
    max_num = max(a, b)

    gcd = 0
    while True:
        r = max_num % min_num

        if r == 0:
            gcd = min_num
            break

        max_num = min_num
        min_num = r
    
    return gcd

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())

    gcd = getGCD(a, b)

    print(int(a * (b/gcd)))