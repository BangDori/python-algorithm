import sys
input = sys.stdin.readline

appleCount, snakeLength = map(int, input().split())
apples = list(map(int, input().split()))
apples.sort()

for apple in apples:
    if snakeLength >= apple: snakeLength += 1
    else: break

print(snakeLength)