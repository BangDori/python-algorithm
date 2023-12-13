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

def dijkstra(start, end):
    heap = [(0, start, str(start))]
    costs[start] = (0, str(start))

    while heap:
        cost, src, move = heapq.heappop(heap)

        if src == end:  
            return

        if costs[src][0] < cost:
            continue

        for next_cost, dst in conn[src]:
            if costs[dst][0] > cost + next_cost:
                costs[dst] = (cost+next_cost, move+" "+str(dst))
                heapq.heappush(heap, (costs[dst][0], dst, move+" "+str(dst)))

costs = [(float('inf'), "") for _ in range(country_count+1)]
dijkstra(start, end)

answer_cost, answer_path = costs[end]
answer_path = answer_path.split()
print(answer_cost, len(answer_path), " ".join(answer_path), sep='\n')