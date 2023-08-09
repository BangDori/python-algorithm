array = [0 for _ in range(42)]
count = 0

for i in range(10):
    num = int(input())

    if array[num % 42] == 0:
        count += 1
    array[num % 42] += 1

print(count)