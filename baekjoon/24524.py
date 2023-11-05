from collections import deque
import sys
input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()

alpha = [deque([]) for _ in range(26)]

for idx in range(len(S)):
    alpha[ord(S[idx])-97].append(idx)

answer = []
for character in T:
    answer.append(alpha[ord(character)-97])

isBreak = False
count = 0
while answer:
    order = []

    if len(answer[0]) == 0:
        break

    order.append(answer[0].popleft())
    for idx in range(1, len(answer)):
        if len(answer[idx]) == 0:
            isBreak = True
            break

        while answer[idx]:
            num = answer[idx].popleft()
            
            if order[-1] < num:
                order.append(num)
                break
        
        if len(order) != idx+1:
            isBreak = True
            break
    
    if isBreak:
        break
    count += 1
print(count)