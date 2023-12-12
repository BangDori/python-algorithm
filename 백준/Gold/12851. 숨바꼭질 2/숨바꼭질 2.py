from collections import deque
import sys
input = sys.stdin.readline

MAX_POS = 100_000
N, K = map(int, input().split())

queue = deque([(N, 0)])
visited = [float('inf') for _ in range(MAX_POS+1)]

answer_time = float('inf')
answer_count = 0

while queue:
    pos, time = queue.popleft()

    if pos == K and time <= answer_time:
        answer_time = time
        answer_count += 1
        continue

    if pos*2 <= MAX_POS and visited[pos*2] >= time:
        visited[pos*2] = time
        queue.append((pos*2, time+1))
    if pos-1 >= 0 and visited[pos-1] >= time:
        visited[pos-1] = time
        queue.append((pos-1, time+1))
    if pos+1 <= MAX_POS and visited[pos+1] >= time:
        visited[pos+1] = time
        queue.append((pos+1, time+1))

print(answer_time, answer_count, sep='\n')