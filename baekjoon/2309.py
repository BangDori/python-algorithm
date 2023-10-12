import sys, itertools
input = sys.stdin.readline

members9 = [int(input()) for _ in range(9)]

answer = []
for members in itertools.combinations(members9, 7):
    if sum(members) == 100:
        answer = list(members)
        break

answer.sort()
for member in answer:
    print(member)