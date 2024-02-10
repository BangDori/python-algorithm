from collections import deque
import sys
input = sys.stdin.readline

RED = 1
BLACK = -1

TC = int(input())

def bfs(src, color):
    queue = deque([])
    queue.append((src, color))

    visited[src] = color
    while queue:
        src, color = queue.popleft()

        for dst in graph[src]:
            if visited[dst] == 0:
                visited[dst] = color * -1
                queue.append((dst, color * -1))
            if visited[dst] == color:
                return False
    
    return True

for _ in range(TC):
    v, e = map(int, input().split())

    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        vA, vB = map(int, input().split())

        graph[vA].append(vB)
        graph[vB].append(vA)
    
    visited = [0 for _ in range(v+1)]
    # cnt = 0
    isBinaryTree = True
    for src in range(1, v+1):
        if visited[src] == 0:
            # cnt += 1

            isBinaryTree = bfs(src, RED)
            if not isBinaryTree:
                break
    
    # if cnt == 2:
    #     print('YES')
    # else:
    if isBinaryTree: print('YES')
    else: print('NO')