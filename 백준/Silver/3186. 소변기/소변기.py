import sys
input = sys.stdin.readline

EXIST = '1'
NOT_EXIST = '0'

K, L, N = map(int, input().split())
state = list(input().rstrip())

isUsed = False
used_time = 0
remain_flush = K
answer = []
for i in range(len(state)):
    if state[i] == EXIST:
        used_time += 1
        if used_time == K:
            isUsed = True

        if isUsed:
            remain_flush = L
    else:
        if not isUsed:
            used_time = 0
            continue

        remain_flush -= 1
        if remain_flush == 0:
            answer.append(i+1)
            used_time = 0
            isUsed = False

if isUsed:
    answer.append(i + 1 + L)

if len(answer) == 0:
    print('NIKAD')
else:
    for ans in answer:
        print(ans)