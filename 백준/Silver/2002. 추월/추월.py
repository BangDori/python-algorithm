from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

tunnel = {}
visited = [False for _ in range(N+1)]
queue = deque([])

# 출입
for i in range(1, N+1):
    carNumber = input().strip()
    tunnel[carNumber] = i
    queue.append(i)

answer = 0
for i in range(1, N+1):
    carNumber = input().strip()

    while visited[queue[0]]:
        queue.popleft()

    if queue[0] == tunnel[carNumber]:
        queue.popleft()
        visited[tunnel[carNumber]] = True
        continue
    
    # 추월
    visited[tunnel[carNumber]] = True
    answer += 1

print(answer)