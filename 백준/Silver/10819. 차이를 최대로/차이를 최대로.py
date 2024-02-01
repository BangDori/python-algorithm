from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

answer = 0
for perm in permutations(numbers, N):
    result = 0

    for i in range(len(perm)-1):
        result += abs(perm[i] - perm[i+1])

    answer = max(answer, result)

print(answer)