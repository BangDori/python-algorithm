import sys
input = sys.stdin.readline

def gcd(num1, num2):
    if num2 > 0:
        return gcd(num2, num1 % num2)
    else:
        return num1

def lcm(num1, num2):
    return num1 * num2 // gcd(num1, num2)

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())

    max_year = lcm(M, N)
    answer = -1
    while x <= max_year:
        if x % N == y % N:
            answer = x
            break
        x += M
    
    print(answer)