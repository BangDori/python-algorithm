import sys
input = sys.stdin.readline

test_case = int(input())
for _ in range(test_case):
    key_logger = input().rstrip()
    
    l_stack = []
    r_stack = []

    for log in key_logger:
        if log == '<':
            if l_stack:
                r_stack.append(l_stack.pop())        
        elif log == '>':
            if r_stack:
                l_stack.append(r_stack.pop())
        elif log == '-':
            if l_stack:
                l_stack.pop()
        else:
            l_stack.append(log)

    r_stack.reverse()
    l_stack += r_stack

    print("".join(l_stack))