from collections import deque
import sys
sys.setrecursionlimit(10 ** 3)
input = sys.stdin.readline

def bfs(a, b):
    queue = deque([(a, "")])
    visited = [False for _ in range(10000)]
    visited[a] = True

    while queue:
        cur, state = queue.popleft()
        
        if cur == b:
            queue.clear()
            return state

        if not visited[(cur*2) % 10000]:
            visited[(cur*2) % 10000] = True
            queue.append(((cur*2) % 10000, state+"D")) # D

        if not visited[(cur-1) % 10000]:
            visited[(cur-1) % 10000] = True
            queue.append(((cur-1) % 10000, state+"S")) # S

        if not visited[cur * 10 % 10000 + cur * 10 // 10000]:
            visited[cur * 10 % 10000 + cur * 10 // 10000] = True
            queue.append((cur * 10 % 10000 + cur * 10 // 10000, state+"L")) # L
        
        if not visited[(cur % 10) * 1000 + (cur // 10)]:
            visited[(cur % 10) * 1000 + (cur // 10)] = True
            queue.append(((cur % 10) * 1000 + (cur // 10), state+"R")) # R

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(bfs(A, B))