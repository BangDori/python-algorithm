from itertools import combinations
import sys
input = sys.stdin.readline

while True:
    numbers = list(map(int, input().split()))
    lotto_cnt = numbers.pop(0)

    if lotto_cnt == 0:
        break

    for lotto in combinations(numbers, 6):
        print(*lotto)
    print()