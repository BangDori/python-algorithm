import sys
from collections import deque
input = sys.stdin.readline

# 큐
queue = deque()
# 명령의 수
N = int(input())

for _ in range(N):
    quiz = input().split()

    command = quiz[0]
    if command == 'push':
        queue.append(quiz[1])
    elif command == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif command == 'size':
        print(len(queue))
    elif command == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    else:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[len(queue)-1])