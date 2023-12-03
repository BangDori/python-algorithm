import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

v, e = map(int, input().split())
visited = [False for _ in range(v+1)]

conn = {}
for i in range(1, v+1):
    conn[i] = []

for _ in range(e):
    src, dst = map(int, input().split())

    conn[src].append(dst)
    conn[dst].append(src)

def dfs(src):
    if visited[src]:
        return
    visited[src] = True

    for dst in conn[src]:
        dfs(dst)

count = 0
for i in range(1, v+1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)