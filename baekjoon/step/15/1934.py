def getLCM(a, b):
    min_num = min(a, b)
    max_num = max(a, b)
    gcd = 1

    while True:
        r = max_num % min_num
        if r == 0:
            gcd = min_num
            break

        max_num = min_num
        min_num = r

    lcm = (a / gcd) * (b / gcd) * gcd
    
    return int(lcm)

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    print(getLCM(A, B))