from collections import deque
import sys
input = sys.stdin.readline

truck_count, load_length, max_weight = map(int, input().split())
trucks = list(map(int, input().split()))
queue = deque()

for truck in trucks:
    queue.append((truck, 1))

moving = deque([])
total_weight = 0
total_time = 1

while queue or moving:
    if queue and total_weight + queue[0][0] <= max_weight:
        total_weight += queue[0][0]
        moving.appendleft(queue.popleft())
    
    for i in range(len(moving)):
        if moving[i][1]+1 > load_length:
            total_weight -= moving[i][0]
            moving.pop()
            continue

        moving[i] = (moving[i][0], moving[i][1]+1)

    total_time += 1

print(total_time)