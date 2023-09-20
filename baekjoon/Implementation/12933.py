import sys
input = sys.stdin.readline

quack = [0, 0, 0, 0, 0]
quiz = list(input().rstrip())

answer = 0
if len(quiz) % 5 != 0:
    answer = -1
else:
    end = []
    running = []

    count = 0
    for idx, alpha in enumerate(quiz):
        if alpha == 'q':
            quack[0] += 1
            running.append(idx)

            if count == 0:
                answer += 1
            else:
                count -= 1
        elif alpha == 'u' and quack[0] > quack[1]:
            quack[1] += 1
        elif alpha == 'a' and quack[1] > quack[2]:
            quack[2] += 1
        elif alpha == 'c' and quack[2] > quack[3]:
            quack[3] += 1
        elif alpha == 'k' and quack[3] > quack[4]:
            quack[4] += 1
            end.append(running.pop(0))
            count += 1

    if len(end) == 0 or len(end) != len(quiz) // 5:
        answer = -1
print(answer)