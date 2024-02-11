import sys
input = sys.stdin.readline

computers = int(input())
lines = int(input())
graph = []

for _ in range(lines):
    a, b, cost = map(int, input().split())
    graph.append((cost, a, b)); graph.append((cost, b, a))

parents = [i for i in range(computers+1)]

def find(child):
    if parents[child] == child: return child
    parents[child] = find(parents[child])
    return find(parents[child])

def union(a, b):
    a, b = find(a), find(b)

    parents[min(a, b)] = max(a, b)

graph.sort()
answer = 0

for cost, a, b in graph:        
    if find(a) != find(b):
        answer += cost
        union(a, b)

print(answer)