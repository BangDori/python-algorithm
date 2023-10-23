from collections import deque
import sys
input = sys.stdin.readline

country_count = int(input())
travel_plane_count = int(input())

conn = {}

for row in range(1, country_count+1):
    line = list(map(int, input().split()))

    conn[row] = []

    for col in range(len(line)):
        if line[col] == 0:
            continue
        
        conn[row].append(col+1)

travel_plane = deque(list(map(int, input().split())))

answer = 1

def dfs(cur, find):
    if cur == find:
        global answer

        answer += 1
        visited.append(cur)
        return
    
    next_conn = conn.get(cur)
    visited.append(cur)

    for next in next_conn:
        if next in visited:
            continue
        dfs(next, find)

for i in range(travel_plane_count-1):
    visited = []
    dfs(travel_plane[i], travel_plane[i+1])

if travel_plane_count == answer:
    print("YES")
else:
    print("NO")