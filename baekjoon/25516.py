import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

edge_count, k = map(int, input().split())
tree = {}

for _ in range(edge_count-1):
    parent, child = map(int, input().split())

    if not tree.get(parent):
        tree[parent] = []
    
    tree[parent].append(child)
apples = list(map(int, input().split()))

answer = 0 if apples[0] == 0 else 1
def dfs(ptr, dist):
    global answer
    if dist >= k:
        return
    
    next_tree = tree.get(ptr)
    if not next_tree:
        return
    for next in next_tree:
        if apples[next] == 1:
            answer += 1
        dfs(next, dist+1)

dfs(0, 0)
print(answer)