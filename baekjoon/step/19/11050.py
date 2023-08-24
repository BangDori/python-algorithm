# 자연수 N, 정수 K
def factorial(N, K):
    fac = 1
    for i in range(N, N-K, -1):
        fac *= i
    
    return fac

N, K = map(int, input().split())

top = factorial(N, K)
bottom = factorial(K, K)

print(int(top / bottom))