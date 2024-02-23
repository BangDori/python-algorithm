from collections import deque
import sys
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(cow_r, cow_c):
    queue = deque([(cow_r, cow_c)])
    
    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < n:
                if visited[nr][nc]: continue
                if (nr, nc) in road[r][c]: continue

                visited[nr][nc] = True
                queue.append((nr, nc))

n, k, r = map(int, input().split())

road = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(r):
    r1, c1, r2, c2 = map(int, input().split())
    r1-=1; c1-=1; r2-=1; c2-=1

    road[r1][c1].append((r2, c2))
    road[r2][c2].append((r1, c1))

cows = []
for _ in range(k):
    cow_r, cow_c = map(int, input().split())
    cow_r-=1; cow_c-=1
    cows.append((cow_r, cow_c))

answer = 0
for i, cow in enumerate(cows):
    visited = [[False] * n for _ in range(n)]
    cow_r, cow_c = cow
    visited[cow_r][cow_c] = True

    bfs(cow_r, cow_c)

    for r2, c2 in cows[i+1:]:
        if not visited[r2][c2]:
            answer += 1

print(answer)