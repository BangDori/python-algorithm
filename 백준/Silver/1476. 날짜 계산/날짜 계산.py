import sys
input = sys.stdin.readline

#  (1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19)

E, S, M = map(int, input().split())
e, s, m = 1, 1, 1

answer = -1

for year in range(1, 7981):
    if e == E and s == S and m == M:
        answer = year
        break

    e += 1; s += 1; m += 1

    if e > 15: e %= 15
    if s > 28: s %= 28
    if m > 19: m %= 19

print(answer)