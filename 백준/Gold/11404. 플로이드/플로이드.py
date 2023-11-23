import sys
input = sys.stdin.readline

N = int(input())
bus_count = int(input())

INF = float('inf')
graph = [[INF for _ in range(N+1)] for _ in range(N+1)]

for _ in range(bus_count):
    src, dst, cost  = map(int, input().split())
    graph[src][dst] = min(graph[src][dst], cost)

for k in range(1, N+1):
    graph[k][k] = 0

    for src in range(1, N+1):
        for dst in range(1, N+1):
            graph[src][dst] = min(graph[src][dst], graph[src][k]+graph[k][dst])

for src in range(1, N+1):
    for dst in range(1, N+1):
        if graph[src][dst] == INF:
            print(0, end=' ')
        else:
            print(graph[src][dst], end=' ')
    print()