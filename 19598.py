import heapq
import sys
input = sys.stdin.readline

meeting_count = int(input())

meeting = []
for _ in range(meeting_count):
    start, end = map(int, input().split())
    meeting.append((start, end))

meeting.sort(key=lambda v: (v[0], v[1]))

current_meeting = [0]
meeting_room = 1

for start, end in meeting:
    if start >= current_meeting[0]:
        heapq.heappop(current_meeting)
    else:
        meeting_room += 1
    heapq.heappush(current_meeting, end)

print(meeting_room)