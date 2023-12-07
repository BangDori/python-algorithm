import heapq
import sys
input = sys.stdin.readline

vertex_count = int(input())

tree = [[] for _ in range(vertex_count+1)]
for _ in range(vertex_count):
    edge_info = list(map(int, input().split()))
    src = edge_info[0]

    for i in range(1, len(edge_info), 2):
        if edge_info[i] == -1:
            break
        
        dst = edge_info[i]
        dist = edge_info[i+1]

        tree[src].append((dist, dst))

distances = [float('inf') for _ in range(vertex_count+1)]
heap = []
def dijkstra(start):
    distances[start] = 0

    heap.append((0, start))
    while heap:
        dist, src = heapq.heappop(heap)

        if distances[src] < dist:
            continue
        
        for next_dist, next in tree[src]:
            if distances[next] > distances[src] + next_dist:
                distances[next] = distances[src] + next_dist
                heap.append((distances[next], next))

dijkstra(1)

v1 = distances.index(max(distances[1:]))
distances = [float('inf') for _ in range(vertex_count+1)]
dijkstra(v1)

print(max(distances[1:]))