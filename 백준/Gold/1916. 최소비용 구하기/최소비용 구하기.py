import heapq
import sys

input = sys.stdin.readline
country_count = int(input())
bus_count = int(input())

INF = float('inf')
costs = [INF for _ in range(country_count+1)]
graph = [[] for _ in range(country_count+1)]

for _ in range(bus_count):
    src, dest, cost = map(int, input().split())
    graph[src].append((dest, cost))

src, dest = map(int, input().split())

def dijkstra(start):
    queue = [(0, start)]

    while queue:
        now_cost, src = heapq.heappop(queue)

        if now_cost > costs[src]:
            continue

        for dest, cost in graph[src]:
            if now_cost + cost < costs[dest]:
                costs[dest] = now_cost + cost
                heapq.heappush(queue, (costs[dest], dest))

dijkstra(src)
print(costs[dest])