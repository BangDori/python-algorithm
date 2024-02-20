from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

visit_count = [1e9 for _ in range(1101)]
queue = deque([(0, 0)])
visit_count[0] = 0

answer = -1
while queue:
    curr, count = queue.popleft()

    if curr >= N-1:
        answer = count
        break

    if visit_count[curr] < count:
        continue
    
    for i in range(1, A[curr]+1):
        if visit_count[curr+i] > count+1:
            visit_count[curr+i] = count+1
            queue.append((curr+i, count+1))

print(answer)