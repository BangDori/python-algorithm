def solution(participant, completion):
    people = {}
    
    
    for c in completion:
        if not people.get(c):
            people[c] = 1
        else:
            people[c] += 1
    
    answer = "hi"
    for p in participant:        
        if not people.get(p) or people.get(p) == 0:
            answer = p
            break
        
        people[p] -= 1
        
    return answer