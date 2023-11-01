from collections import deque
import sys
input = sys.stdin.readline

test_case = int(input().rstrip())
for _ in range(test_case):
    func = input().rstrip()
    array_length = int(input().rstrip())
    array = deque(input().rstrip().split(','))

    if func.count('D') > array_length:
        print('error')
        continue

    array[0] = array[0][1:]
    array[-1] = array[-1][:-1]

    isReverse = False

    for i in func:
        if i == 'D' and not isReverse:
            array.popleft()

        if i == 'D' and isReverse:
            array.pop()

        if i == 'R':
            isReverse = not isReverse
    
    if isReverse:
        array.reverse()

    print('[', ",".join(array), "]", sep='')