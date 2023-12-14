from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# 0 -> 내부 공기
# 1 -> 치즈
# 2 -> 외부 공기

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def get_cheese(row, col):
    cheese = deque([])

    for r in range(row):
        for c in range(col):
            if matrix[r][c] == 1:
                cheese.append((r, c))
    
    return cheese

def repaint_matrix(x, y, matrix):
    queue = deque([(0, 0)])
    visited = [[False] * col for _ in range(row)]
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny]:
                visited[nx][ny] = True
                if matrix[nx][ny] != 1:
                    matrix[nx][ny] = 2
                    queue.append((nx, ny))
    

def bfs(row, col, cheese, matrix):
    melt, keep = deque([]), deque([])

    while cheese:
        x, y = cheese.popleft()

        count = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < row and 0 <= ny < col and matrix[nx][ny] == 2:
                count += 1

        if count >= 2:
            melt.append((x, y))
        else:
            keep.append((x, y))
    
    return melt, keep

def remove_melt(melt):
    while melt:
        x, y = melt.popleft()
        matrix[x][y] = 2

def solution(row, col, matrix):
    cheese = get_cheese(row, col)
    time = 0

    while cheese:
        repaint_matrix(0, 0, matrix)
        melt, keep = bfs(row, col, cheese, matrix)

        remove_melt(melt)
        cheese = keep
        time += 1

    return time

row, col = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(row)]

print(solution(row, col, matrix))