def solution(priorities, location):
    answer = 0
    keys = [0] * 10
    
    for idx, priority in enumerate(priorities):
        keys[priority] += 1
    
    prev_key = 0
    for idx in range(9, -1, -1):
        if keys[idx] == 0:
            continue
        
        for _ in range(keys[idx]):
            if not priorities[prev_key:].count(idx):
                prev_key = 0
            find_loc = priorities.index(idx, prev_key)
            prev_key = find_loc
            priorities[find_loc] = -1
            answer += 1
                        
            if location == find_loc:
                return answer
        
            
    return answer