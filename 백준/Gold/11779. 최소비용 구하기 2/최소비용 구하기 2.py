import heapq
import sys
input = sys.stdin.readline

country_count = int(input())
bus_count = int(input())
conn = {}
for i in range(1, country_count+1):
    conn[i] = []

for _ in range(bus_count):
    src, dst, cost = map(int, input().split())
    conn[src].append((cost, dst))

start, end = map(int, input().split())
nodes = [-1 for _ in range(country_count+1)]

def dijkstra(start, end):
    heap = [(0, start)]
    costs[start] = 0

    while heap:
        cost, src= heapq.heappop(heap)

        if src == end:  
            return

        if costs[src] < cost:
            continue

        for next_cost, dst in conn[src]:
            if costs[dst] > cost + next_cost:
                costs[dst] = cost+next_cost
                nodes[dst] = src
                heapq.heappush(heap, (costs[dst], dst))

costs = [float('inf') for _ in range(country_count+1)]
dijkstra(start, end)

answer_cost = costs[end]
answer_path = []
while nodes[end] != -1:
    answer_path.append(end)
    end = nodes[end]
answer_path.append(start)

print(answer_cost, len(answer_path), sep='\n')
for _ in range(len(answer_path)):
    print(answer_path.pop(), end=' ')