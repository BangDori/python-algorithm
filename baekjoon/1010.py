# 자연수 N, 정수 K
def factorial(N, K):
    fac = 1
    for i in range(N, N-K, -1):
        fac *= i
    
    return fac

T = int(input())

for _ in range(T):
    # 서쪽 (N), 동쪽 (M)
    N, M = map(int, input().split())

    top = factorial(M, N)
    bottom = factorial(N, N)

    print(int(top/bottom))