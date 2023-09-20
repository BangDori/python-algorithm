import sys
input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    number_count = int(input())
    numbers = list(map(int, input().split()))

    print(min(numbers), max(numbers))