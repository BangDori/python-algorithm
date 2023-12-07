from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

max_distance = 100_001
queue = deque([(N, 0)])
visited = [False for _ in range(max_distance)]
visited[N] = True

while queue:
    cur, time = queue.popleft()

    if cur == K:
        print(time)
        break

    if cur*2 < max_distance and not visited[cur*2]:
        visited[cur*2] = True
        queue.append((cur*2, time))
    if cur-1 >= 0 and not visited[cur-1]:
        visited[cur-1] = True
        queue.append((cur-1, time+1))
    if cur+1 < max_distance and not visited[cur+1]:
        visited[cur+1] = True
        queue.append((cur+1, time+1))