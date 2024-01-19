from collections import deque
import sys
input = sys.stdin.readline

# 1: A + 1
# 2: A * 2

prev, next = map(int, input().split())
visited = [float('inf') for _ in range(1_000_001)]

queue = deque([(prev, 0)])
answer = 0

while queue:
    curr, count = queue.popleft()

    if curr == next:
        print(count)
        break

    if visited[curr] <= count:
        continue
    visited[curr] = count

    if curr * 2 <= next and visited[curr*2] > count+1:
        queue.append((curr*2, count+1))

    if curr + 1 <= next and visited[curr+1] > count+1:
        queue.append((curr+1, count+1))