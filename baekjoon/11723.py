import sys
input = sys.stdin.readline

numbers = [0 for _ in range(21)]
op_count = int(input())

for _ in range(op_count):
    op = list(input().split())

    if op[0] == 'add':
        numbers[int(op[1])] = True
    elif op[0] == 'remove':
        numbers[int(op[1])] = False
    elif op[0] == 'check':
        if numbers[int(op[1])]:
            print(1)
        else:
            print(0)
    elif op[0] == 'toggle':
        numbers[int(op[1])] = not numbers[int(op[1])]
    elif op[0] == 'all':
        for i in range(1, 21):
            numbers[i] = True
    else:
        for i in range(1, 21):
            numbers[i] = False