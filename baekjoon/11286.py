import heapq, sys
input = sys.stdin.readline

heap = []
N = int(input())

for _ in range(N):
    x = int(input())

    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
        continue

    heapq.heappush(heap, (abs(x), x))