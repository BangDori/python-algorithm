import sys
input = sys.stdin.readline

MAX_LEN = 10001

def d(num):
    number = num

    while num >= 1:
        number += num % 10
        num //= 10

    return number

isSelfNumber = [True for _ in range(MAX_LEN)]

for i in range(1, MAX_LEN):
    num = d(i)
    if num >= MAX_LEN: continue
    isSelfNumber[num] = False

for i in range(1, MAX_LEN):
    if isSelfNumber[i]:
        print(i)