import sys
input = sys.stdin.readline

def find(x):
    if parent[x] == x: return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    px, py = find(x), find(y)
    parent[max(px, py)] = min(px, py)

while True:
    M, N = map(int, input().split())
    if M == 0 and N == 0:
        break

    parent = [i for i in range(M + 1)]
    edges = []
    
    for i in range(N):
        x, y, z = map(int, input().split())
        edges.append((z, x, y))

    edges.sort()

    unused_light = 0
    for edge in edges:
        z, x, y = edge

        if find(x) != find(y): union(x, y)
        else: unused_light += z
    
    print(unused_light)