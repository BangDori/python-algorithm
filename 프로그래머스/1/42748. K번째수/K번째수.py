def solution(array, commands):
    answer = []
    
    for command in commands:
        start, end, pos = command
        new_array = array[start-1:end]
        
        new_array.sort()        
        answer.append(new_array[pos-1])
        
    return answer