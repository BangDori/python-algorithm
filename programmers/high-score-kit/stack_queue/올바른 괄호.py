def solution(s):
    answer = True
    stack = []
    
    if s[0] == ')':
        return False
    
    for alpha in s:
        stack.append(alpha)
        
        if stack[len(stack)-2] == '(' and stack[len(stack)-1] == ')':
            stack.pop()
            stack.pop()
        
    if len(stack) != 0:
        answer = False
        
    return answer