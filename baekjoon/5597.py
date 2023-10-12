attendances = [False for _ in range(31)]
count = 0

for _ in range(28):
    std = int(input())

    attendances[std] = True

for i in range(1, 31):
    if not attendances[i]:
        print(i)
        count += 1

    if count == 2:
        break