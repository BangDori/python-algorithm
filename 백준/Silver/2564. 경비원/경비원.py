from collections import deque
import sys
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

def get_pos(dir, pos):
    if dir == 1: return 0, pos
    elif dir == 2: return row-1, pos
    elif dir == 3: return pos, 0
    
    return pos, col-1

col, row = map(int, input().split())
col += 1; row += 1

board = [[0] * col for _ in range(row)]
store_cnt = int(input())
store = []

# 상점의 위치
for _ in range(store_cnt):
    dir, pos = map(int, input().split())
    s_row, s_col = get_pos(dir, pos)
    store.append((s_row, s_col))

# 동근이의 위치
dir, pos = map(int, input().split())
d_row, d_col = get_pos(dir, pos)

# 최소 거리 구하기
visited = [[float('inf')] * col for _ in range(row)]
queue = deque([(d_row, d_col, 0)])
visited[d_row][d_col] = 0

while queue:
    r, c, dist = queue.popleft()

    for i in range(4):
        nr = dr[i] + r
        nc = dc[i] + c

        if 0 <= nr < row and 0 <= nc < col and visited[nr][nc] > dist+1:
            if nr == 0 or nr == row-1 or nc == 0 or nc == col-1:
                visited[nr][nc] = dist+1
                queue.append((nr, nc, dist+1))

answer = 0
for sr, sc in store:
    answer += visited[sr][sc]

print(answer)