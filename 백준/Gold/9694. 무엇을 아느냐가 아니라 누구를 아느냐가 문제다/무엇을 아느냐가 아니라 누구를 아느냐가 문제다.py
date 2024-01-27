from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def dijkstra(start, end):
    heap = [(0, start, [start])]
    visited = [float('inf') for _ in range(end)]

    visited[start] = 0
    while heap:
        dist, src, people = heappop(heap)

        if src == end-1:
            return people

        if visited[src] < dist:
            continue
        visited[src] = dist

        for extra_dist, dst in graph[src]:
            if dist + extra_dist < visited[dst]:
                heappush(heap, (dist + extra_dist, dst, people + [dst]))

    return -1

TC = int(input())
for tid in range(1, TC+1):
    N, M = map(int, input().split())

    graph = [[] for _ in range(M)]
    for _ in range(N):
        x, y, z = map(int, input().split())
        graph[x].append((z, y))
        graph[y].append((z, x))
    
    answer = dijkstra(0, M)
    if answer == -1:
        print(f"Case #{tid}:", -1)    
    else:
        print(f"Case #{tid}:", *answer)