n = int(input())
c = input().split()
min = int(c[0])

for i in range(2, len(c)):
    if min > int(c[i]):
        min = int(c[i])

print(min)