"""
    1 sec, 512 MB
    동적 프로그래밍과, 재귀 호출 비교
"""

import sys
input = sys.stdin.readline

fibo_answer = 0
fibo2_answer = 0

def fibo(n):
    global fibo_answer

    if n == 1 or n == 2:
        fibo_answer += 1
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    
def fibo2(n):
    global fibo2_answer
    f[1] = f[2] = 1

    for i in range(3, n+1):
        fibo2_answer += 1
        f[i] = f[i-1] + f[i-2]

    return f[n]

N = int(input())
f = [0 for _ in range(N+1)]

fibo(N); fibo2(N)
print(fibo_answer, fibo2_answer)