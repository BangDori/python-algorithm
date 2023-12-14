import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())

conn = {}
for i in range(1, V+1):
    conn[i] = []

for _ in range(E):
    src, dst, cost = map(int, input().split())
    conn[src].append((cost, dst))
    conn[dst].append((cost, src))

required_v1, required_v2 = map(int, input().split())

def dijkstra(start, end):
    heap = [(0, start)]
    costs = [float('inf') for _ in range(V+1)]
    costs[start] = 0

    while heap:
        cost, src = heapq.heappop(heap)

        if src == end:
            return costs[end]

        if costs[src] < cost:
            continue
        
        for next_cost, dst in conn[src]:
            tot_cost = next_cost + cost

            if costs[dst] > tot_cost:
                costs[dst] = tot_cost
                heapq.heappush(heap, (tot_cost, dst))

    return float('inf')

path1 = dijkstra(1, required_v1) + dijkstra(required_v1, required_v2) + dijkstra(required_v2, V)
path2 = dijkstra(1, required_v2) + dijkstra(required_v2, required_v1) + dijkstra(required_v1, V)
answer = min(path1, path2)

if answer == float('inf'):
    print(-1)
else:
    print(answer)