from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0]
subin, find = map(int, input().split())

visited = [False for _ in range(100001)]
queue = deque([(subin, 0)])
while queue:
    cur, time = queue.popleft()

    if cur == find:
        print(time)
        break

    for i in range(3):
        nx = cur + dx[i]

        if i == 2:
            nx *= 2
        
        if 0 <= nx < 100001 and not visited[nx]:
            # print(nx)
            visited[nx] = True
            queue.append((nx, time+1))