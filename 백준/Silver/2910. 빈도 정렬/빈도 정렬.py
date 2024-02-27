import sys
input = sys.stdin.readline

N, C = map(int, input().split())
number_count = {}
number_index = {}
numbers = list(map(int, input().split()))

for index, number in enumerate(numbers):
    if not number_count.get(number):
        number_count[number] = numbers.count(number)
    if not number_index.get(number):
        number_index[number] = index+1

numbers.sort(key=lambda v: (-number_count[v], number_index[v]))

print(*numbers)