import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

node, water = map(int, input().split())
graph = {}
visited = {}

for _ in range(node-1):
    u, v = map(int, input().split())

    if not graph.get(u): graph[u] = []
    if not graph.get(v): graph[v] = []

    graph[u].append(v)
    graph[v].append(u)

leaf_node = 0

def dfs(u):
    global leaf_node

    if visited.get(u):
        return
    visited[u] = True

    is_leaf = True
    for v in graph[u]:
        if not visited.get(v):
            is_leaf = False
            dfs(v)
    
    if is_leaf:
        leaf_node += 1

dfs(1)
print(water / leaf_node)