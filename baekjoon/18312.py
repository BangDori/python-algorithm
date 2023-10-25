import sys
input = sys.stdin.readline

hour, num = map(int, input().split())
time = [0, 0, 0]

def find_num(num):
    if time[0] % 10 == num or time[0] // 10 == num:
        return 1
    
    if time[1] % 10 == num or time[1] // 10 == num:
        return 1
    
    if time[2] % 10 == num or time[2] // 10 == num:
        return 1
    
    return 0

answer = 0
while time[0] != hour+1:
    count = find_num(num)

    answer += count
    time[2] += 1

    if time[2] == 60:
        time[1] += 1
        time[2] = 0
    
    if time[1] == 60:
        time[0] += 1
        time[1] = 0

print(answer)
