import sys
input = sys.stdin.readline

LEFT_SIGN = '>'
RIGHT_SIGN = '<'

k = int(input())
signs = list(input().split())

answer = [[10] * (k+1) for _ in range(2)]

# 최댓값 구하기
for i in range(k+1):
    number = -1

    for num in range(9, -1, -1):
        if not num in answer[0]:
            number = num
            break

    for sign in signs[i:]:
        if sign == LEFT_SIGN:
            break
        number -= 1
    
    answer[0][i] = number

# 최솟값 구하기
for i in range(k+1):
    number = -1

    for num in range(10):
        if not num in answer[1]:
            number = num
            break

    for sign in signs[i:]:
        if sign == RIGHT_SIGN:
            break
        number += 1
    
    answer[1][i] = number

for ans in answer:
    print(*ans, sep='')