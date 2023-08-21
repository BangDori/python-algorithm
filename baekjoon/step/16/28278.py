# 1 x : 정수 X를 스택에 삽입
# 2: 스택의 맨 위의 정수 빼기, None => -1
# 3: 정수의 개수 출력
# 4: isEmpty
# 5: 스택의 맨 위 정수 출력

import sys
input = sys.stdin.readline

stack = []
N = int(input())

for _ in range(N):
    command = list(map(int, input().split()))


    if command[0] == 1:
        stack.append(command[1])
    elif command[0] == 2:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 3:
        print(len(stack))
    elif command[0] == 4:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])