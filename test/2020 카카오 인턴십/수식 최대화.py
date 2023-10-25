from itertools import permutations

def get_result(op_order, numbers, ops):
    new_numbers = numbers.copy()
    new_ops = ops.copy()
    
    for op in op_order:
        idx = 0
        while idx < len(new_ops):           
            if new_ops[idx] == op:                
                num1 = new_numbers.pop(idx)
                num2 = new_numbers.pop(idx)
                
                num1 = int(num1)
                num2 = int(num2)
                
                if op == '-':
                    new_numbers.insert(idx, num1-num2)
                elif op == '*':
                    new_numbers.insert(idx, num1*num2)
                elif op == '+':
                    new_numbers.insert(idx, num1+num2)
                new_ops.pop(idx)
                continue
            idx += 1
    
    return new_numbers.pop()

def solution(expression):
    numbers = []
    ops = []
    unique_op = []
    
    start = 0
    for i in range(len(expression)):
        if expression[i] in ['+', '-', '*']:
            numbers.append(expression[start:i])
            ops.append(expression[i])
            start = i+1
            
            if not expression[i] in unique_op:
                unique_op.append(expression[i])
    numbers.append(expression[start:])


    answer = 0
    for op_order in permutations(unique_op, len(unique_op)):
        result = get_result(op_order, numbers, ops)
        
        if abs(result) > answer:
            answer = abs(result)
            
    return answer