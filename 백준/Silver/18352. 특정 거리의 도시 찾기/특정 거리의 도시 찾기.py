from collections import deque
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

visited = [1e9 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
for _ in range(M):
    src, dst = map(int, input().split())
    graph[src].append(dst)

queue = deque([(X, 0)])
visited[X] = 0

while queue:
    src, dist = queue.popleft()

    if visited[src] < dist: continue

    for dst in graph[src]:
        if visited[dst] > dist + 1:
            visited[dst] = dist + 1
            queue.append((dst, dist+1))

answer = []
for cid in range(N+1):
    if visited[cid] == K:
        answer.append(cid)

if len(answer) == 0: print(-1)
else:
    for ans in answer:
        print(ans)