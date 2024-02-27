import sys
input = sys.stdin.readline

total_round, jimin, hansoo = map(int, input().split())

answer = 0
while jimin != hansoo:
    # 다음 경기
    jimin -= jimin // 2
    hansoo -= hansoo // 2

    answer += 1

print(answer)