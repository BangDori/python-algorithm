import sys
input = sys.stdin.readline

answer = -1

def dfs(x, y, count):
    global answer
    if count == answer:
        return
    
    people = person_dic.get(x)

    if people.count(y):
        answer = count
        return
    
    for p in people:
        person_dic[p].remove(x)
        dfs(p, y, count+1)
        person_dic[p].append(x)
    
    return

people_count = int(input())
quiz_x, quiz_y = map(int, input().split())

person_dic = {}
hint_count = int(input())
for _ in range(hint_count):
    person_x, person_y = map(int, input().split())

    if not person_dic.get(person_x):
        person_dic[person_x] = [person_y]
    else:
        person_dic[person_x].append(person_y)
    
    if not person_dic.get(person_y):
        person_dic[person_y] = [person_x]
    else:
        person_dic[person_y].append(person_x)

for li in person_dic.values():
    li.sort()

dfs(quiz_x, quiz_y, 1)
print(answer)