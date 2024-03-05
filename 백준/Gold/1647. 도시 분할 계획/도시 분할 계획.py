import sys
input = sys.stdin.readline

def find(a):
    if a == parents[a]: return a
    parents[a] = find(parents[a])
    return parents[a]

def union(a, b):
    pa, pb = find(a), find(b)

    parents[min(pa, pb)] = max(pa, pb)

N, C = map(int, input().split())

parents = [i for i in range(N+1)]
graph = []

for _ in range(C):
    a, b, cost = map(int, input().split())
    graph.append((cost, a, b))

graph.sort()
answer = []

for cost, a, b in graph:
    pa, pb = find(a), find(b)
    if pa != pb:
        union(a, b)
        answer.append(cost)

answer.pop()
print(sum(answer))