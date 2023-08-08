n = int(input())
c = input().split()

std = [0 for _ in range(24)]

for i in range(0, len(c)):
    std[int(c[i])] += 1

for i in range(1, 24):
    print(std[i], end=' ')