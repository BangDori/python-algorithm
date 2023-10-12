import sys
input = sys.stdin.readline

A, B = map(int, input().split())

answer = 0
while B > A:
    answer += 1
    if B % 2 == 0:
        B //= 2
        continue

    if B % 10 == 1:
        B //= 10
        continue

    break

if A != B:
    answer = -1
else:
    answer += 1
print(answer)