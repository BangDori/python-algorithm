from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

nodes = int(input())
conns = [deque([]) for _ in range(nodes+1)]
tree = [0 for _ in range(nodes+1)]

for _ in range(nodes-1):
    a, b = map(int, input().split())

    conns[a].append(b)
    conns[b].append(a)

tree[1] = 1

def dfs(i):
    while conns[i]:
        node = conns[i].popleft()

        if tree[node] == 0:
            tree[node] = i
            dfs(node)

dfs(1)
for idx in range(2, nodes+1):
    print(tree[idx])