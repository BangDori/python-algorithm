from collections import deque
import sys
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, K = map(int, input().split())
virus = [list(map(int, input().split())) for _ in range(N)]
s, x, y = map(int, input().split())

vids = [[] for _ in range(K+1)]
for row in range(N):
    for col in range(N):
        if virus[row][col] != 0:
            vids[virus[row][col]].append((row, col))

queue = deque([])
time = 0
for vid in vids:
    queue += vid

while queue and time < s:
    next_queue = deque([])

    while queue:
        row, col = queue.popleft()

        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]

            if 0 <= nr < N and 0 <= nc < N and virus[nr][nc] == 0:
                virus[nr][nc] = virus[row][col]
                next_queue.append((nr, nc))

    queue = next_queue
    time += 1

print(virus[x-1][y-1])