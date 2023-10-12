from collections import deque
import sys
input = sys.stdin.readline

x, y, z = map(int, input().split())
box = [[[] for _ in range(y)] for _ in range(z)]

# ←, ↑, →, ↓, z+1, z-1
nx = [-1, 0, 1, 0, 0, 0]
ny = [0, 1, 0, -1, 0, 0]
nz = [0, 0, 0, 0, -1, 1]

completed = deque()

for zdx in range(z):
    for ydx in range(y):
        tomatoes = list(map(int, input().split()))
        
        if tomatoes.count(1):
            for xdx in range(x):
                if tomatoes[xdx] == 1:
                    completed.append((zdx, ydx, xdx))
        
        box[zdx][ydx] = tomatoes

time = 0
while len(completed) > 0:
    time += 1

    completed_size = len(completed)

    for _ in range(completed_size):
        cur_z, cur_y, cur_x = completed.popleft()

        box[cur_z][cur_y][cur_x] = 1

        for idx in range(6):
            next_z = cur_z + nz[idx]
            next_y = cur_y + ny[idx]
            next_x = cur_x + nx[idx]
            
            if 0 <= next_x < x and 0 <= next_y < y and 0 <= next_z < z:
                if box[next_z][next_y][next_x] == 0:
                    completed.append((next_z, next_y, next_x))
                    box[next_z][next_y][next_x] = 1

for zdx in range(z):
    for ydx in range(y):
        for xdx in range(x):
            if box[zdx][ydx][xdx] == 0:
                print(-1)
                sys.exit(0)

print(time-1)