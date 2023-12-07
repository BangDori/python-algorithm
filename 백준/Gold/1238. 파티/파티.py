import heapq
import sys
input = sys.stdin.readline

INF = float('inf')

people, load_count, x = map(int, input().split())

load = [[] for _ in range(people+1)]
for _ in range(load_count):
    src, dst, time = map(int, input().split())
    load[src].append((time, dst))


heap = []
def dijkstra(i, array):
    array[i] = 0
    heap.append((0, i))

    while heap:
        time, src = heapq.heappop(heap)

        if array[src] < time:
            continue

        for next_time, next in load[src]:
            if time + next_time < array[next]:
                array[next] = time + next_time
                heapq.heappush(heap, (array[next], next))

back = [INF for _ in range(people+1)]
dijkstra(x, back)

answer = 0
for i in range(1, people+1):
    go = [INF for _ in range(people+1)]
    dijkstra(i, go)
    answer = max(answer, go[x] + back[i])

print(answer)