import heapq, sys
input = sys.stdin.readline

heap = []
N = int(input())

answer = 0
for _ in range(N):
    x = int(input())

    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
        continue

    heapq.heappush(heap, x)