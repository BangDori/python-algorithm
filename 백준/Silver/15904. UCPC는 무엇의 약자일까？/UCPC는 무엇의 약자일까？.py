import sys
input = sys.stdin.readline

UCPC = "UCPC"
inputString = list(input().strip())

i = 0
for alpha in inputString:
    if i >= 4: break

    if alpha == UCPC[i]:
        i += 1
        continue

if i >= 4: print("I love UCPC")
else: print("I hate UCPC")