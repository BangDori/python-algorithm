from collections import deque
import sys
input = sys.stdin.readline
N = int(input())

queue = deque()

def pop():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue.popleft())

def isEmpty():
    if len(queue) == 0:
        print(1)
    else:
        print(0)

def front():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[0])

def back():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[len(queue) - 1])

for _ in range(N):
    command = list(input().split())

    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        pop()
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        isEmpty()
    elif command[0] == 'front':
        front()
    else:
        back()