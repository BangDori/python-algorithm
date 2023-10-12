import sys
input = sys.stdin.readline

train_count, command_line = map(int, input().split())
train = [[0] * 20 for _ in range(train_count)]

for _ in range(command_line):
    commands = list(map(int, input().split()))
    command = commands[0]
    train_idx = commands[1] - 1

    if command == 1:
        seat_idx = commands[2] - 1
        # 사람을 태우기
        train[train_idx][seat_idx] = 1
    elif command == 2:
        # 사람 하차
        seat_idx = commands[2] - 1
        train[train_idx][seat_idx] = 0
    elif command == 3:
        # 모두 뒤로

        for idx in range(19):
            train[train_idx][19-idx] = train[train_idx][18-idx]
        train[train_idx][0] = 0
    else:
        # 모두 앞으로
        for idx in range(19):
            train[train_idx][idx] = train[train_idx][idx+1]
        train[train_idx][19] = 0

# 기차들을 비교 후, 다른 기차들을 출력
star = ""
for row in range(train_count):
    current_star = ""
    for col in range(20):
        current_star += str(train[row][col])
    
    if star.find(current_star) == -1:
        star += current_star
        star += " "

answer = len(star.split())
print(answer)