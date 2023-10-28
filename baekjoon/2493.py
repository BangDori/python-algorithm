import sys
input = sys.stdin.readline

size = int(input())
table = list(map(int, input().split()))
answer = [0 for _ in range(size)]

stack = []

for idx in range(size):
    if not stack:
        answer[idx] = 0
        stack.append((idx+1, table[idx]))
    else:
        while stack:
            if stack[-1][1] < table[idx]:
                stack.pop()
            else:
                break
        
        if stack:
            answer[idx] = stack[-1][0]
        else:
            answer[idx] = 0
        stack.append((idx+1, table[idx]))

for ans in answer:
    print(ans, end=' ')