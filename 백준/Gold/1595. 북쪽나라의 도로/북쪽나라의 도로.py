import heapq
import sys
input = sys.stdin.readline

load_info = [[] for _ in range(10_001)]
buildings = set()

while True:
    try:
        src, dst, cost = map(int, input().split())
        buildings.add(src); buildings.add(dst)

        load_info[src].append((-cost, dst))
        load_info[dst].append((-cost, src))
    except:
        break

if len(buildings) == 0:
    print(0)
else:
    def dijkstra(start):
        heap = []
        heap.append((0, start))
        visited[start] = 1

        while heap:
            cost, src = heapq.heappop(heap)

            if cost > visited[src]:
                continue

            visited[src] = cost

            for next_cost, dst in load_info[src]:
                if visited[dst] == 0 and dst != start:
                    visited[dst] = cost + next_cost
                    heapq.heappush(heap, (cost + next_cost, dst))

        return -min(visited)

    visited = [0 for _ in range(10_001)]
    dijkstra(1)
    
    start_point = visited.index(min(visited), 1)
    visited = [0 for _ in range(10_001)]
    print(dijkstra(start_point))