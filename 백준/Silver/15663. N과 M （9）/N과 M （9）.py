from itertools import permutations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

unique_array = set()
for comb in permutations(array, M):
    unique_array.add(comb)

new_array = list(unique_array)
new_array.sort(key=lambda v: v)
for numbers in new_array:
    for number in numbers:
        print(number, end=' ')
    print()