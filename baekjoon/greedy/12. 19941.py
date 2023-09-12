import sys
input = sys.stdin.readline

size, distance = map(int, input().split())
quiz = list(input().rstrip())
burger = [idx for idx in range(len(quiz)) if quiz[idx] == 'H']

answer = 0
for idx in range(len(quiz)):
    if quiz[idx] == 'H':
        continue

    for bIdx in range(len(burger)):
        if burger[bIdx] < idx - distance:
            continue

        if burger[bIdx] > idx + distance:
            break

        answer += 1
        burger.pop(bIdx)
        break
print(answer)