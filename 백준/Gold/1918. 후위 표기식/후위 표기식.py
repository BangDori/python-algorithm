import sys
input = sys.stdin.readline

formula = input().rstrip()

op = {}
op['+'] = 1; op['-'] = 1
op['*'] = 2; op['/'] = 2
op['('] = 3; op[')'] = 4

stack = []

answer = ""
for sign in formula:
    if sign >= 'A' and sign <= 'Z':
        answer += sign
    else:
        if sign == '(':
            stack.append(sign)
        elif sign == ')':
            while stack:
                if stack[-1] == '(':
                    stack.pop()
                    break
                answer += stack.pop()
        else:
            while stack:
                if stack[-1] != '(' and op[stack[-1]] >= op[sign]:
                    answer += stack.pop()
                else:
                    break
            stack.append(sign)

while stack:
    answer += stack.pop()

print(answer)