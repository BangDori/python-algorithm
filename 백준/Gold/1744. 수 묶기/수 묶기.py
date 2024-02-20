import sys
input = sys.stdin.readline

def bundle(array):
    result = 0

    for i in range(0, len(array), 2):
        if i >= len(array)-1: result += array[i]
        else:
            result += array[i] * array[i+1]

    return result

N = int(input())
numbers = [int(input()) for _ in range(N)]
positive, negative = [], []

result = 0
for number in numbers:
    if number > 1:
        positive.append(number)
    elif number <= 0:
        negative.append(number)
    else:
        result += 1

positive.sort(reverse=True)
negative.sort()

result += bundle(positive)
result += bundle(negative)

print(result)