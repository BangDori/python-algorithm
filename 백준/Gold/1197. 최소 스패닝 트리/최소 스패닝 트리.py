import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

v, e = map(int, input().split())
parent = [i for i in range(v+1)]
graph = []

def find(a):
    if a == parent[a]: return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    pa, pb = find(a), find(b)
    parent[max(pa, pb)] = min(pa, pb)

for _ in range(e):
    src, dst, cost = map(int, input().split())
    graph.append((cost, src, dst))

graph.sort()
answer = 0

for cost, src, dst in graph:
    ps, pd = find(src), find(dst)
    if ps != pd:
        union(src, dst)
        answer += cost

print(answer)