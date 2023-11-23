import heapq
import sys

input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())
K = int(input())

weights = [INF for _ in range(V+1)]
graph = [[] for _ in range(V+1)]
heap = []

for _ in range(E):
    src, dst, weight = map(int, input().split())
    graph[src].append((weight, dst))

def dijkstra(start):
    # 현재 위치와 이동 거리
    weights[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        tot_weight, now = heapq.heappop(heap)

        if weights[now] < tot_weight:
            continue

        for weight, dst in graph[now]:
            next_weight = tot_weight + weight

            if weights[dst] > next_weight:
                weights[dst] = next_weight
                heapq.heappush(heap, (next_weight, dst))

dijkstra(K)
for i in range(1, V+1):
    print("INF" if weights[i] == INF else weights[i])