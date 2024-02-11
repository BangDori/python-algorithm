import sys
input = sys.stdin.readline

N, L = map(int, input().split())
tapes = list(map(int, input().split()))
tapes.sort()

start = tapes.pop(0)
count = 1

for pos in tapes:
    if pos in range(start, start+L): continue

    start = pos
    count += 1

print(count)
