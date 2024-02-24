import sys
input = sys.stdin.readline

N = int(input())

peoples = []
people_count = 0
for _ in range(N):
    pos, people = map(int, input().split())
    peoples.append((pos, people))
    people_count += people

peoples.sort()

answer = 1
current_count = 0
for pos, people in peoples:
    current_count += people

    if current_count >= people_count / 2:
        answer = pos
        break

print(answer)