import heapq
import sys
input = sys.stdin.readline

INSERT = 'I'
DELETE = 'D'
EMPTY = 'EMPTY'

T = int(input())
for _ in range(T):
    k = int(input())
    min_heap = [] # 양수
    max_heap = [] # 음수
    exist_number = {}
    
    for _ in range(k):
        command, n = input().rstrip().split()
        n = int(n)

        if command == INSERT:
            if not exist_number.get(n):
                exist_number[n] = 0
            exist_number[n] += 1
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, n * -1)
        else:
            if n == 1: # 최대값 삭제
                if len(max_heap) != 0:
                    while max_heap:
                        if exist_number[max_heap[0] * -1] == 0:
                            heapq.heappop(max_heap)
                            continue
                        
                        max_num = heapq.heappop(max_heap)
                        exist_number[max_num * -1] -= 1
                        break
            else: # 최소값 제거
                if len(min_heap) != 0:
                    while min_heap:
                        if exist_number[min_heap[0]] == 0:
                            heapq.heappop(min_heap)
                            continue

                        min_num = heapq.heappop(min_heap)
                        exist_number[min_num] -= 1
                        break
    
    keys = list(exist_number.keys())
    keys.sort()
    exist = []

    for key in keys:
        if exist_number[key]:
            exist.append(key)
    
    if len(exist) == 0:
        print(EMPTY)
    else:
        print(max(exist), min(exist))