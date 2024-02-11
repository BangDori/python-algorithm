from itertools import permutations
import sys
input = sys.stdin.readline

question_cnt = int(input())
numbers = list(permutations([str(i+1) for i in range(9)], 3))

for _ in range(question_cnt):
    number, strike, ball = map(int, input().split())
    number = list(str(number))

    removed_numbers = []
    for compare in numbers:
        strike_cnt = 0; ball_cnt = 0

        for i in range(3):
            if number[i] == compare[i]: strike_cnt += 1
            elif number[i] in compare: ball_cnt += 1
            
        if strike_cnt != strike or ball_cnt != ball:
            removed_numbers.append(compare)

    for removed_number in removed_numbers:
        numbers.remove(removed_number)

print(len(numbers))