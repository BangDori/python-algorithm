import sys
input = sys.stdin.readline

N = int(input())

cows = [-1] * 11
answer = 0
for _ in range(N):
    id, loc = map(int, input().split())

    if cows[id] == -1:
        cows[id] = loc
        continue

    if cows[id] != loc:
        cows[id] = loc
        answer += 1

print(answer)