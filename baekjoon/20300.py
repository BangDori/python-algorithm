import sys
input = sys.stdin.readline

health_count = int(input())
loss = list(map(int, input().split())) 

loss.sort()

max_loss = 0
if len(loss) % 2 == 1:
    max_loss = loss.pop()

answer = 0
for idx in range(len(loss)//2):
    loss_sum = loss[idx] + loss[-(idx+1)]

    if loss_sum > answer:
        answer = loss_sum

if max_loss > answer:
    answer = max_loss
print(answer)