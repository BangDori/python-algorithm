import sys
input = sys.stdin.readline

height = int(input())
visit = list(map(int, input().split()))
tree = [0 for _ in range(2**height)]

left = 0
right = len(visit)

def dfs(left, right, depth, n):
    if depth == height:
        return
    
    mid = (left+right)//2
    tree[2**depth+n] = visit[mid]

    dfs(left, mid, depth+1, 2*n) # Left
    dfs(mid, right, depth+1, 2*n+1) # Right

dfs(left, right, 0, 0)

line_breaking = 2
for idx in range(1, len(tree)):
    if idx == line_breaking-1:
        line_breaking *= 2
        print(tree[idx])
    else:
        print(tree[idx], end=' ')