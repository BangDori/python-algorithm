# 1 000 000 000
# 22-1 = 3
# 33-1 = 8
# 44-1 = 15
# 55-1 = 24
# 66-1 = 35
# 77-1 = 48
# 88-1 = 63
# 99-1 = 80
# 10 10 -1 = 99
# 11 11 -1 = 120
# 12 12 -1 = 143
# 13 13 -1 = 168

# 1 3 6 10 15 21 28 36 45

import sys
input = sys.stdin.readline

def isSquare(x):
    if x ** 0.5 == int(x ** 0.5):
        return True
    
    return False

case = 1
while True:
    min, max = map(int, input().split())

    if min == 0 and max == 0:
        break
    
    pos = 0
    while pos * (pos+1) // 2 < min:
        pos += 1
    
    count = 0
    while pos * (pos+1) // 2 < max-1:
        cur = pos * (pos+1) // 2 + 1
        if isSquare(cur): count += 1
        pos += 1
    
    print('Case ', case, ': ', count, sep='')
    case += 1