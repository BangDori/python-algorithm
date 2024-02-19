def solution(answers):
    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    answer = []
    
    people = { 1: 0, 2: 0, 3: 0 }
    for i, number in enumerate(answers):
        if person1[i % len(person1)] == number: people[1] += 1
        if person2[i % len(person2)] == number: people[2] += 1
        if person3[i % len(person3)] == number: people[3] += 1
    
    success_count = max(people.values())
    
    for pid in people.keys():
        if people[pid] == success_count:
            answer.append(pid)
    
    return answer