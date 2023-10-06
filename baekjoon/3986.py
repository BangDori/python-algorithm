import sys
input = sys.stdin.readline
 
n = int(input())
answer = 0
 
for _ in range(n):
    word = input().rstrip()
    stack = []
 
    for idx in range(len(word)):
        if stack and word[idx] == stack[-1]:
            stack.pop()
        else:
            stack.append(word[idx])
 
    if not stack:
        answer += 1
print(answer)