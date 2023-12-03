from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

result = deque([])
for _ in range(N):
    result.append(int(input()))

stack = []
numbers = [N-i for i in range(N)]
answer = []
while numbers or stack:
    if stack and stack[-1] == result[0]:
        answer.append('-')
        result.popleft()
        stack.pop()
        continue

    if len(numbers) == 0:
        break
    number = numbers.pop()
    stack.append(number)
    answer.append('+')

if len(stack) == 0 and len(numbers) == 0:
    print("\n".join(answer))
else:
    print("NO")