from collections import deque
import sys
input = sys.stdin.readline

queue = deque()
N = int(input())

for _ in range(N):
    command = input().split()
    type = int(command[0])

    if type == 1:
        # Front 삽입
        queue.appendleft(command[1])
    elif type == 2:
        # Back 삽입
        queue.append(command[1])
    elif type == 3:
        # 맨 앞의 정수 빼고 출력 or -1
        if len(queue) > 0:
            print(queue.popleft())
        else:
            print(-1)
    elif type == 4:
        # 맨 뒤의 정수 빼고 출력 or -1
        if len(queue) > 0:
            print(queue.pop())
        else:
            print(-1)
    elif type == 5:
        # 정수의 개수
        print(len(queue))
    elif type == 6:
        # isEmpty ? 1 : 0
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif type == 7:
        # 맨 앞의 정수가 있다면 맨 앞의 정수 or -1
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)
    elif type == 8:
        # 맨 뒤의 정수가 있다면 매 뒤의 정수 or -1
        if len(queue) > 0:
            print(queue[len(queue) - 1])
        else:
            print(-1)