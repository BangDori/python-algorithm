import math

def isPrime(num):
    if num == 2:
        return True
    if num == 1 or num % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(num)+1), 2):
        if num % i == 0:
            return False
        
    return True

M, N = map(int, input().split())

for num in range(M, N+1):
    if isPrime(num):
        print(num)