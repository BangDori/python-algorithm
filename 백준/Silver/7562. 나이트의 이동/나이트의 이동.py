from collections import deque
import sys
input = sys.stdin.readline

dr = [-1, -2, -2, -1, 1, 2, 2, 1]
dc = [-2, -1, 1, 2, 2, 1, -1, -2]
INF = float('inf')

TC = int(input())
answer = []

for _ in range(TC):
    size = int(input())
    visited = [[INF] * size for _ in range(size)]

    start_r, start_c = list(map(int, input().split()))
    end_r, end_c = map(int, input().split())

    queue = deque([(start_r, start_c, 0)])
    visited[start_r][start_c] = 0

    while queue:
        row, col, cnt = queue.popleft()

        if row == end_r and col == end_c:
            answer.append(cnt)
            break

        if visited[row][col] < cnt:
            continue
        visited[row][col] = cnt

        for i in range(8):
            nr = row + dr[i]
            nc = col + dc[i]

            if 0 <= nr < size and 0 <= nc < size and visited[nr][nc] > cnt+1:
                visited[nr][nc] = cnt+1
                queue.append((nr, nc, cnt+1))

for ans in answer:
    print(ans)