import math
import sys
input = sys.stdin.readline

MOD = 1000000007

def getExpectedValue(n, s):
    return s * getSquaredNumber(n, MOD-2) % MOD

def getSquaredNumber(num, exp):
    if exp == 1:
        return num

    if exp % 2 == 0:
        half = getSquaredNumber(num, exp//2)
        return half * half % MOD
    else:
        return num * getSquaredNumber(num, exp - 1) % MOD
    
m = int(input())
sum = 0
for _ in range(m):
    n, s = map(int, input().split())
    gcd = math.gcd(n, s)
    n //= gcd; s //= gcd

    sum += getExpectedValue(n, s)
    sum %= MOD

print(sum)