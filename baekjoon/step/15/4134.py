import math

def isPrime(num):
    for i in range(3, int(math.sqrt(num)+1), 2):
        if num % i == 0:
            return False
    
    return True

t = int(input())

for _ in range(t):
    n = int(input())

    if n == 0 or n == 1 or n == 2:
        print(2)
        continue

    if n % 2 == 0:
        n += 1

    for i in range(n, 2*n, 2):        
        if isPrime(i):
            print(i)
            break
