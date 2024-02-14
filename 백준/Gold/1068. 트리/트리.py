import sys
sys.setrecursionlimit(10 ** 2)
input = sys.stdin.readline

N = int(input())
node_list = list(map(int, input().split()))
remove_node = int(input())

def dfs(node):
    global leaf_node
    if node == remove_node:
        return
    
    if not parent.get(node):
        leaf_node += 1
        return
    
    for child in parent.get(node):
        if len(parent.get(node)) == 1 and child == remove_node:
            leaf_node += 1
            continue
        dfs(child)

parent = {}
root = -1

for i, node in enumerate(node_list):
    if node == -1:
        root = i
        continue

    if not parent.get(node):
        parent[node] = []
    parent[node].append(i)

leaf_node = 0
dfs(root)
print(leaf_node)