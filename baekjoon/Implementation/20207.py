import sys
input = sys.stdin.readline

todos_count = int(input())
todos = [0 for _ in range(366)]

min_start = sys.maxsize
min_end = 0

for idx in range(todos_count):
    start, end = map(int, input().split())

    if start < min_start:
        min_start = start
    if min_end < end:
        min_end = end

    for day in range(start, end+1):
        todos[day] += 1

answer = 0
col = 0
row = 0
cur = 0
for day in range(min_start, min_end+1):
    if todos[day] == 0:
        answer += (col * row)
        col = 0
        row = 0
    else:
        col += 1
        row = max(row, todos[day])

if col != 0:
    answer += (col * row)
print(answer)