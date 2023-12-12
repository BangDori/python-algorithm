import sys
input = sys.stdin.readline

people, party_count = map(int, input().split())
truthly = list(map(int, input().split()))[1:]

tid = truthly[0] if len(truthly) > 0 else -1

conn = [i for i in range(people+1)]
party = []

def union(a, b):
    a = find(a)
    b = find(b)

    if a in truthly and b in truthly:
        return
    if a in truthly:
        conn[b] = a
    elif b in truthly:
        conn[a] = b
    else:
        if a > b:
            conn[a] = b
        else:
            conn[b] = a

def find(i):
    if conn[i] == i:
        return i
    
    conn[i] = find(conn[i])
    return find(conn[i])

for i in range(len(truthly)-1):
    union(truthly[i], truthly[i+1])

for _ in range(party_count):
    members = list(map(int, input().split()))[1:]

    for i in range(len(members)-1):
        union(members[i], members[i+1])
    party.append(members)

answer = 0
if tid == -1:
    answer = len(party)
else:
    for members in party:
        isTruthly = False
        for member in members:
            if find(member) in truthly:
                isTruthly = True
                break
        
        if not isTruthly:
            answer += 1

print(answer)