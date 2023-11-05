import sys
input = sys.stdin.readline

N = int(input())
limits = list(map(int, input().split()))
limits.sort()

if N == 1:
    print(1)
else:
    max_limit = limits.pop()
    tot = 0
    
    for idx in range(len(limits)):
        tot += limits[idx]
    
    if tot >= max_limit:
        print(tot + max_limit)
    else:
        print(2*tot + 1)