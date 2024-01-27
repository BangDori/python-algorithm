import sys
input = sys.stdin.readline

# ↓, →, ↑, ←
# 0, 1, 2, 3

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

col, row = map(int, input().split())
matrix = [list(map(bin, map(int, input().split()))) for _ in range(row)]

def conversion_matrix():
    for r in range(row):
        for c in range(col):
            matrix[r][c] = matrix[r][c][2:].zfill(4)

def dfs(r, c, sid):
    cnt = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < row and 0 <= nc < col and matrix[r][c][i] == '0' and visited[nr][nc] == 0:
            visited[nr][nc] = sid
            cnt += dfs(nr, nc, sid)
    
    return cnt

def docking(r, c, sid):
    max_section = -1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < row and 0 <= nc < col and visited[nr][nc] != sid:
            max_section = max(max_section, section[visited[nr][nc]-1] + section[sid-1])
    
    return max_section

conversion_matrix()

visited = [[0] * col for _ in range(row)]
section = []
for r in range(row):
    for c in range(col):
        if visited[r][c]:
            continue
        visited[r][c] = len(section)+1
        cnt = dfs(r, c, len(section)+1)
        section.append(cnt)

max_section = 0
for r in range(row):
    for c in range(col):
        max_section = max(max_section, docking(r, c, visited[r][c]))

print(len(section)) # 방 개수
print(max(section)) # 가장 넓은 방의 크기
print(max_section) # 벽 하나 제거했을 때 얻을 수 있는 가장 넓은 방의 크기