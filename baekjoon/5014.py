from collections import deque
import sys
input = sys.stdin.readline

total, current, startlink, up, down = map(int, input().split())
dx = [up, -down]

visited = [False for _ in range(total+1)]
queue = deque([(current, 0)])

answer = -1
while queue:
    floor, count = queue.popleft()

    if floor == startlink:
        answer = count
        break

    for i in range(2):
        nfloor = floor + dx[i]

        if 0 < nfloor <= total and not visited[nfloor]:
            visited[nfloor] = True
            queue.append((nfloor, count+1))

if answer == -1:
    print("use the stairs")
else:
    print(answer)