import heapq
import sys
input = sys.stdin.readline

N = int(input())
edu_times = []

for _ in range(N):
    start, end = map(int, input().split())
    edu_times.append((start, end))

edu_times.sort()
edu_rooms = [edu_times[0][1]] # 끝나는 시간
edu_times.pop(0)

for next_start_time, next_end_time in edu_times:
    if edu_rooms[0] <= next_start_time:
        heapq.heappop(edu_rooms)
    heapq.heappush(edu_rooms, next_end_time)

print(len(edu_rooms))