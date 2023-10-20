import sys
input = sys.stdin.readline

meeting_count = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(meeting_count)]
meetings.sort(key=lambda v: (v[1], v[0], v[1]-v[0]))

current_start = meetings[0][0]
current_end = meetings[0][1]
count = 1

for i in range(1, len(meetings)):
    next_start, next_end = meetings[i]
    
    if current_end <= next_start:
        current_end = next_end
        count += 1
        continue

    if current_start >= next_end:
        current_start = next_start
        count += 1
        continue

print(count)