CYCLE = 8

finger_pos = int(input())
use_count = int(input())

answer = -1
if use_count == 0: answer = finger_pos - 1
elif finger_pos == 1: answer = CYCLE * use_count
elif finger_pos == 5: answer = CYCLE * use_count + 4
else:
    answer = CYCLE * ((use_count+1)//2)

    if use_count % 2 == 0: answer += (finger_pos - 1)
    else: answer -= (finger_pos - 1)

print(answer)