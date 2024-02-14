import sys
input = sys.stdin.readline

S = int(input())
tot = 0
num = 1

while tot < S:
    tot += num
    num += 1

    if tot == S:
        num -= 1
        break
    if tot > S:
        num -= 2
        break

print(num)