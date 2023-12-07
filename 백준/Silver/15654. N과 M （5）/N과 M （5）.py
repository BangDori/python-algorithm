from itertools import permutations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

for comb in permutations(array, M):
    for num in comb:
        print(num, end=' ')
    print()