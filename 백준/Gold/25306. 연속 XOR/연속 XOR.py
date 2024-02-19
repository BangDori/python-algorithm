a, b = map(int, input().split())

def func(n):
    start = n//4 * 4
    answer = 0

    for i in range(start, n+1):
        answer ^= i

    return answer

print(func(a-1) ^ func(b))