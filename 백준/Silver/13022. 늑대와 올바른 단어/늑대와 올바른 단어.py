import sys
input = sys.stdin.readline

input_wolf = input().rstrip()

isEnable = True
wolf_list = []
for i in range(1, 14):
    wolf = 'w' * i + 'o' * i + 'l' * i + 'f' * i
    wolf_list.append(wolf)

pos = 0
while pos < len(input_wolf):
    temp = False

    for wolf_item in wolf_list:
        if pos + len(wolf_item) <= len(input_wolf) and input_wolf[pos:pos+len(wolf_item)] == wolf_item:
            pos += len(wolf_item)
            temp = True
            break

    if not temp:
        isEnable = False
        break

print(1 if isEnable else 0)