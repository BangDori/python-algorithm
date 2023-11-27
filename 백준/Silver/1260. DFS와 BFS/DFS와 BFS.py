from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(v):
    if visited[v]:
        return
    visited[v] = True
    
    print(v, end=' ')
    vertexs = graph[v]
    for next in vertexs:
        dfs(next)

def bfs(v):
    visited = [False for _ in range(vertex+1)]
    visited[v] = True

    queue = deque([v])
    while queue:
        cur = queue.popleft()
        print(cur, end=' ')

        vertexs = graph[cur]
        for next in vertexs:
            if not visited[next]:
                queue.append(next)
                visited[next] = True

vertex, edge, start = map(int, input().split())
graph = {}

for v in range(1, vertex+1):
    graph[v] = []

for _ in range(edge):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for v in range(1, vertex+1):
    graph[v].sort()

visited = [False for _ in range(vertex+1)]
dfs(start)
print()

bfs(start)