import heapq
import sys
input = sys.stdin.readline

INF = float('inf')

people, load_count, X = map(int, input().split())
load = [[] for _ in range(people+1)]
heap = []

for _ in range(load_count):
    src, dst, time = map(int, input().split())
    load[src].append((time, dst))

end = [INF for _ in range(people+1)]

def dijkstra(start, array):
    # 현재 위치와 이동 거리
    array[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        tot_time, now = heapq.heappop(heap)

        if array[now] < tot_time:
            continue

        for time, dst in load[now]:
            next_time = tot_time + time

            if array[dst] > next_time:
                array[dst] = next_time
                heapq.heappush(heap, (next_time, dst))

dijkstra(X, end)

answer = 0
for i in range(1, len(end)):
    start = [INF for _ in range(people+1)]
    dijkstra(i, start)
    answer = max(answer, start[X]+end[i])
print(answer)