import sys
input = sys.stdin.readline

input_string = list(input().rstrip())

slide_size = input_string.count('a')
if slide_size == 0:
    print(0)
else:
    input_string += input_string[:-1]

    min_count = sys.maxsize
    for i in range(len(input_string)-slide_size+1):
        min_count = min(min_count, input_string[i:i+slide_size].count('b'))
    print(min_count)