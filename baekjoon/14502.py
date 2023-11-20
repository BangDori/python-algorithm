from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

size_x, size_y = map(int, input().split())
section = [list(map(int, input().split())) for _ in range(size_x)]

virus = deque([])
empty_section = []
for x in range(size_x):
    for y in range(size_y):
        if section[x][y] == 2:
            virus.append((x, y))
        
        if section[x][y] == 0:
            empty_section.append((x, y))

column_list = deque([])
for column in combinations(empty_section, 3):
    column_list.append(column)

answer = 0
while column_list:
    columns = column_list.popleft()
    section_copy = [[section[x][y] for y in range(size_y)] for x in range(size_x)]
    safe_section_count = len(empty_section)-3

    for x, y in columns:
        section_copy[x][y] = 1
    
    virus_copy = virus.copy()
    while virus_copy:
        x, y = virus_copy.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < size_x and 0 <= ny < size_y and section_copy[nx][ny] == 0:
                safe_section_count -= 1
                section_copy[nx][ny] = 2
                virus_copy.append((nx, ny))
    
    answer = max(answer, safe_section_count)

print(answer)