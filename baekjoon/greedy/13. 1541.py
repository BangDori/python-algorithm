import sys
input = sys.stdin.readline

quiz = input().rstrip().split('-')

answer = 0
for idx, q in enumerate(quiz):
    if q.find('+') != -1:
        numbers = q.split('+')
        sum = 0
        for num in numbers:
            sum += int(num)

        answer += sum if idx == 0 else -sum
        continue

    answer += int(q) if idx == 0 else -int(q)

print(answer)