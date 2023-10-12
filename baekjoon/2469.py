import sys
input = sys.stdin.readline

participant = int(input().rstrip())
rows = int(input().rstrip())

people = [chr(65+idx) for idx in range(participant)]
result = list(input().rstrip())
ladder = []
isReverse = False # ? 시작

def change_pos(idx, array):
    temp = array[idx]
    array[idx] = array[idx+1]
    array[idx+1] = temp

for _ in range(rows):
    row = list(input().rstrip())

    if row[0] == '?':
        isReverse = True
        continue

    if not isReverse:
        for idx, col in enumerate(row):
            if col == '*':
                continue
            change_pos(idx, people)
    else:
        ladder.append(row)

ladder.reverse()

for row in ladder:
    for idx, col in enumerate(row):
        if col == '*':
            continue
        change_pos(idx, result)

answer = ['*'] * (participant-1)

idx = 0
while idx < len(people):
    if people[idx] == result[idx]:
        idx += 1
        continue

    if idx < len(people)-1 and people[idx] == result[idx+1] and people[idx+1] == result[idx]:
        answer[idx] = '-'
        idx += 2
        continue

    break

if idx >= len(people):
    print("".join(answer))
else:
    print("x" * (participant-1))