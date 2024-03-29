from itertools import combinations
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

answer = 0
for i in range(1, N+1):
    for perm in combinations(numbers, i):
        if sum(perm) == S:
            answer += 1

print(answer)