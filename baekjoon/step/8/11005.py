import math

n, b = map(int, input().split())
s = ''

while n >= 1:
    if n%b >= 10:
        s += chr(55+math.floor(n%b))
    else:
        s += str(math.floor(n%b))
    n /= b

print(s[::-1])