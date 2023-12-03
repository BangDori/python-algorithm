import heapq
import sys
input = sys.stdin.readline

test_case = int(input())
for _ in range(test_case):
    N, M = map(int, input().split())
    docs = list(map(int, input().split()))

    for i in range(len(docs)):
        docs[i] = (docs[i]*-1, i)

    heapq.heapify(docs)
    
    count = 0
    prev_index = -1
    while docs:
        priority, index = heapq.heappop(docs)
        if index > prev_index:
            count += 1
            prev_index = index
        else:
            heapq.heappush(docs, (priority, index+N))
            continue

        if index % N == M:
            print(count)
            break