import sys
input = sys.stdin.readline

def getGCD(diffs):
    gcd = 1

    min_diff = min(diffs)
    while True:
        for diff in diffs:
            r = diff % min_diff
            if r != 0:
                min_diff = r
                break
                
        if r == 0:
            gcd = min_diff
            break
    
    return gcd

n = int(input())
trees = [int(input()) for _ in range(n)]
diffs = []

for i in range(1, len(trees)):
    diffs.append(trees[i] - trees[i-1])

gcd = getGCD(diffs)

count = 0
for diff in diffs:
    count += int(diff / gcd) - 1
print(count)