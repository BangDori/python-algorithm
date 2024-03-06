import sys
input = sys.stdin.readline

def find(x):
    if x == parents[x]: return x
    parents[x] = find(parents[x])
    return parents[x]

def union(v1, v2):
    pv1, pv2 = find(v1), find(v2)
    parents[max(pv1, pv2)] = min(pv1, pv2)

current_case = 0
answer = []

while True:
    current_case += 1
    vertex, edge = map(int, input().split())

    if vertex == 0 and edge == 0: break

    parents = [i for i in range(vertex+1)]
    cycle = set()
    for _ in range(edge):
        v1, v2 = map(int, input().split())
        pv1, pv2 = find(v1), find(v2)

        if pv1 != pv2: union(v1, v2)
        else: cycle.add(v1); cycle.add(v2); cycle.add(pv1)
        
        if pv1 in cycle or pv2 in cycle:
            cycle.add(v1); cycle.add(v2)

    root = set()
    for v in range(1, vertex+1):
        pv = find(v)
        if pv in cycle: continue        
        root.add(pv)
    
    tree_count = len(root)
    if tree_count == 0: answer.append(f'Case {current_case}: No trees.')
    elif tree_count == 1: answer.append(f'Case {current_case}: There is one tree.')
    else: answer.append(f'Case {current_case}: A forest of {tree_count} trees.')

for ans in answer:
    print(ans)