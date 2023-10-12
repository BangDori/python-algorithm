import math

size = 1000000
isPrime = [True] * size

isPrime[0] = isPrime[1] = False
ssize = int(size ** 0.5)
for i in range(2, ssize+1):
    if isPrime[i]:
        for j in range(i+i, size, i):
            isPrime[j] = False

prime = [i for i in range(2, size) if isPrime[i]]

T = int(input())

for i in range(T):
    N = int(input())
    count = 0

    # j + sec = N
    for j in range(len(prime)):
        if prime[j] >= N:
            break
        sec = N - prime[j]

        if isPrime[sec]:
            count += 1
    
    print(math.ceil(count/2))