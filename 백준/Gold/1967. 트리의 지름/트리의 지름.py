import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

node = int(input())
tree = {}
for i in range(node):
    tree[i] = []

for _ in range(node-1):
    src, dst, length = map(int, input().split())
    src -= 1
    dst -= 1

    tree[src].append((dst, length))
    tree[dst].append((src, length))

def dfs(i, total_length):
    if visited[i]:
        return
    visited[i] = True
    length[i] = total_length

    for n, l in tree[i]:
        if length[n] > total_length + l:
            length[n] = total_length + l
            dfs(n, length[n])

answer = 0
visited = [False for _ in range(node)]
length = [sys.maxsize for _ in range(node)]
dfs(0, 0)

max_node = length.index(max(length))
visited = [False for _ in range(node)]
length = [sys.maxsize for _ in range(node)]
dfs(max_node, 0)
print(max(length))