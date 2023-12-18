import heapq
import sys
input = sys.stdin.readline

region_count, search_range, edge_count = map(int, input().split())
items = [0] + list(map(int, input().split()))

graph = [[] for _ in range(region_count+1)]

for _ in range(edge_count):
    src, dst, search_length = map(int, input().split())
    graph[src].append((search_length, dst))
    graph[dst].append((search_length, src))
    
def dijkstra(start):
    heap = [(0, start)]
    cost[start] = 0

    while heap:
        move, src = heapq.heappop(heap)

        if cost[src] < move:
            continue

        for next_move, dst in graph[src]:
            if move + next_move < cost[dst]:
                cost[dst] = move+next_move
                heapq.heappush(heap, (cost[dst], dst))
        
answer = 0
for i in range(1, region_count+1):
    cost = [float('inf') for _ in range(region_count+1)]
    dijkstra(i)

    total_item = 0
    for k, c in enumerate(cost):
        if c <= search_range:
            total_item += items[k]
    
    answer = max(answer, total_item)

print(answer)