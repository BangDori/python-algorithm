def printLCM(a, b):
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
    
    lcm = gcd * (a / gcd) * (b / gcd)
    return int(lcm)

A, B = map(int, input().split())
print(printLCM(A, B))