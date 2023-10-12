import sys
input = sys.stdin.readline

def manipulate_man(num):
    for idx in range(num-1, len(switchs), num):
        if switchs[idx] == 0:
            switchs[idx] = 1
            continue

        switchs[idx] = 0

def manipulate_woman(num):
    left_pos = right_pos = num-1

    while True:
        if left_pos <= 0 or right_pos >= len(switchs)-1:
            break

        if switchs[left_pos-1] != switchs[right_pos+1]:
            break

        left_pos -= 1
        right_pos += 1

    if left_pos == right_pos:
        if switchs[right_pos] == 0:
            switchs[right_pos] = 1
        else:
            switchs[right_pos] = 0

        return

    for idx in range(left_pos, right_pos+1):
        if switchs[idx] == 0:
            switchs[idx] = 1
        else:
            switchs[idx] = 0
      
switch_count = int(input().rstrip())
switchs = list(map(int, input().rstrip().split()))

student_count = int(input().rstrip())

# 남학생 (1), 여학생 (2)
for _ in range(student_count):
    gender, num = map(int, input().rstrip().split())

    if gender == 1:
        manipulate_man(num)

    if gender == 2:
        manipulate_woman(num)

for switch in switchs:
    print(switch)