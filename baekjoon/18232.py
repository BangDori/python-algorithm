from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1]

N, M = map(int, input().split())
start, end = map(int, input().split())
visited = [300001 for _ in range(N+1)]
teleport = {}

for _ in range(M):
    x, y = map(int, input().split())

    if not teleport.get(x):
        teleport[x] = []
    if not teleport.get(y):
        teleport[y] = []
    
    teleport[x].append(y)
    teleport[y].append(x)

def bfs():
    queue = deque([(start, 0)])
    visited[start] = 0

    while queue:
        pos, time = queue.popleft()
        
        if pos == end:
            return time
        
        for i in range(2):
            next = pos + dx[i]

            if 1 <= next <= N and visited[next] > time+1:
                visited[next] = time+1
                queue.append((next, time+1))
        
        if teleport.get(pos):
            for move in teleport.get(pos):
                next = move

                if 1 <= next <= N and visited[next] > time+1:
                    visited[next] = time+1
                    queue.append((next, time+1))
    
    return 0

answer = bfs()
print(answer)