import sys
input = sys.stdin.readline

PUSH = 'push'
POP = 'pop'
SIZE = 'size'
EMPTY = 'empty'
TOP = 'top'

stack = []
N = int(input())

for _ in range(N):
    command = input().split()

    if command[0] == PUSH:
        stack.append(command[1])
    elif command[0] == POP:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == SIZE:
        print(len(stack))
    elif command[0] == EMPTY:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])