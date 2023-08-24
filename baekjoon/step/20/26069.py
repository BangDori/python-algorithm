# 사람들이 만난 기록의 수 (N)
N = int(input())
people = { 'ChongChong': True }

for _ in range(N):
    a, b = input().split()

    if not people.get(a) and not people.get(b):
        continue

    if people.get(a) and not people.get(b):
        people[b] = True
    
    if not people.get(a) and people.get(b):
        people[a] = True
    
print(len(people))