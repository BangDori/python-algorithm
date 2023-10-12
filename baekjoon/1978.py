n = int(input())
list = list(map(int, input().split()))
list = [i for i in list if ((i % 2 != 0) & ((i != 1))) | (i == 2)]

count = 0
for i in list:
    isPrime = True
    for j in range(3, i):
        if i % j == 0:
            isPrime = False
            break
    
    if isPrime:
        count += 1

print(count)