import math

a, r, n = input().split()

a = int(a)
r = int(r)
n = int(n)

print(math.floor(a * math.pow(r, n-1)))