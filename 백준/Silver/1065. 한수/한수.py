import sys
input = sys.stdin.readline

def isOneNumber(num):
    diff = (num % 100) // 10 - num % 10

    while num >= 10:
        if (num % 100) // 10 - num % 10 == diff:
            num //= 10
        else:
            return False
    
    return True

N = int(input())

answer = 0
for num in range(1, N+1):
    if num < 100:
        answer += 1
    elif isOneNumber(num):
        answer += 1

print(answer)