import sys
input = sys.stdin.readline

numbers = [True] * (123456 * 2 + 1)

numbers[0] = numbers[1] = False

size = int(len(numbers) ** 0.5)
for i in range(2, size+1):
    if numbers[i]:
        for j in range(i+i, len(numbers), i):
            numbers[j] = False

while True:
    n = int(input())

    if n == 0:
        break

    count = 0
    for i in range(n+1, 2*n+1):
        if numbers[i]:
            count += 1
    print(count)