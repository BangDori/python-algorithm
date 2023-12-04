from itertools import product
import sys
input = sys.stdin.readline

channel = input().rstrip()
broken_count = int(input())
broken_remocon = list(map(int, input().split())) if broken_count != 0 else []

current = 100

remocon = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for broken_num in broken_remocon:
    remocon.remove(broken_num)

if int(channel) == current:
    print(0)
else:
    answer = abs(current - int(channel))
    count = abs(current - int(channel))

    for i in range(1, 7):
        for numbers in product(remocon, repeat=i):
            result = 0

            for num in numbers:
                result *= 10
                result += num

            if abs(int(channel) - result) < answer and count > len(numbers) + abs(int(channel)-result):
                answer = abs(int(channel) - result)
                count = len(numbers) + abs(int(channel) - result)

    print(count)