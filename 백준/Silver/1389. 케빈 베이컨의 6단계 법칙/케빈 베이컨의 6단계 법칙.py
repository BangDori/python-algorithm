from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

conn = {}
for i in range(N):
    conn[i] = []

for _ in range(M):
    src, dst = map(int, input().split())

    src -= 1; dst -= 1
    conn[src].append(dst); conn[dst].append(src)


baken = [0 for _ in range(N)]
for i in range(N):
    costs = [-1 for _ in range(N)]
    costs[i] = 0

    queue = deque([(i, 0)])
    while queue:
        cur, cost = queue.popleft()

        for next in conn[cur]:
            if costs[next] == -1:
                costs[next] = cost+1
                queue.append((next, cost+1))
    
    baken[i] = sum(costs)

print(baken.index(min(baken))+1)