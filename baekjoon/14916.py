"""
    2 sec, 512 MB

    2원 5원 짜리의 거스름돈

    최소한의 거스름돈
"""

import sys
input = sys.stdin.readline

amount = int(input())

money5 = amount // 5
money2 = 0

answer = 0
while True:
    if money5 == 0 and amount % 2 == 1:
        answer = -1
        break
    if (amount - (5 * money5)) % 2 == 0:
        money2 = (amount - 5 * money5) // 2
        answer = money5 + money2
        break

    money5 -= 1
print(answer)