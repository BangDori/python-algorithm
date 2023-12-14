import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

MOD = 1000000007

f = {}
f[0] = 0; f[1] = f[2] = 1

def fibo(n):
    if f.get(n):
        return f[n]
    else:
        res = 0

        if n % 2 == 0:
            res = fibo(n//2+1) ** 2 - fibo(n//2-1) ** 2
            f[n] = res % MOD
        else:
            res = fibo(n//2) ** 2 + fibo(n//2+1) ** 2
            f[n] = res % MOD

        return f[n]

def solution(n):
    answer = fibo(n)
    return answer

N = int(input())
print(solution(N))