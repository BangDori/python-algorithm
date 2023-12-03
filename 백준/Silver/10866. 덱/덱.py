from collections import deque
import sys
input = sys.stdin.readline

PUSH_FRONT = 'push_front'
PUSH_BACK = 'push_back'
POP_FRONT = 'pop_front'
POP_BACK = 'pop_back'
SIZE = 'size'
EMPTY = 'empty'
FRONT = 'front'
BACK = 'back'

queue = deque([])
N = int(input())

for _ in range(N):
    inputs = input().split()

    command = inputs[0]

    if command == PUSH_FRONT:
        queue.appendleft(inputs[1])
    elif command == PUSH_BACK:
        queue.append(inputs[1])
    elif command == POP_FRONT:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif command == POP_BACK:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())
    elif command == SIZE:
        print(len(queue))
    elif command == EMPTY:
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command == FRONT:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif command == BACK:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])