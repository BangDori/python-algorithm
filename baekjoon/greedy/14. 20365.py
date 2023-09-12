import sys
input = sys.stdin.readline

length = int(input())
quiz = input()

removed_R = quiz.replace('R', " ").split()
removed_B = quiz.replace('B', " ").split()

answer = 1
if len(removed_R) > len(removed_B):
    answer += len(removed_B)
else:
    answer += len(removed_R)

print(answer)