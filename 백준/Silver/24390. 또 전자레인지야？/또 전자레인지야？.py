from collections import deque
import sys
input = sys.stdin.readline

ON = 0
OFF = 1

time = list(map(int, input().split(":")))
required_time = time[0] * 60 + time[1]

visited = [float('inf') for _ in range(3601)]

# 현재 시간, 클릭 횟수, 전자레인지 구동 시간
queue = deque([(10, 1, OFF), (60, 1, OFF), (600, 1, OFF), (30, 1, ON)])

answer = float('inf')
while queue:
    curr_time, click_cnt, status = queue.popleft()

    if curr_time == required_time: answer = min(answer, click_cnt + status)
    if curr_time > required_time or click_cnt >= visited[curr_time]:
        continue
    visited[curr_time] = click_cnt

    if curr_time + 10 <= 3600 and visited[curr_time+10] > click_cnt + 1:
        queue.append((curr_time+10, click_cnt+1, status))
    if curr_time + 60 <= 3600 and visited[curr_time+60] > click_cnt + 1:
        queue.append((curr_time+60, click_cnt+1, status))
    if curr_time + 600 <= 3600 and visited[curr_time+600] > click_cnt + 1:
        queue.append((curr_time+600, click_cnt+1, status))
    if curr_time + 30 <= 3600 and visited[curr_time+30] > click_cnt + 1:
        queue.append((curr_time+30, click_cnt+1, ON))

print(answer)