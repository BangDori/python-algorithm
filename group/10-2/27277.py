import sys
input = sys.stdin.readline

people = int(input())
skill = list(map(int, input().split()))
skill.sort()

if people == 1:
    print(skill[0])
else:
    performance = [skill.pop()]

    while len(skill) > 0:
        if len(skill) >= 2:
            min_skill = skill.pop(0)
            max_skill = skill.pop()
            
            performance.append(min_skill)
            performance.append(max_skill)
        else:
            performance.append(skill.pop())

    answer = performance[0]

    for idx in range(1, len(performance)):
        answer += max(0, performance[idx] - performance[idx-1])
    print(answer)