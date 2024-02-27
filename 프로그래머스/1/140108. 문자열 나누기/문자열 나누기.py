def solution(s):
    answer = 0
    stack = []
    
    for alpha in s:
        if not stack or stack[-1] == alpha:
            stack.append(alpha)
        else:
            stack.pop()
            
            if len(stack) == 0:
                answer += 1
    
    if len(stack) > 0: answer += 1
    return answer