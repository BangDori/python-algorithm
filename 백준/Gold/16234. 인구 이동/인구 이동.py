from collections import deque
import sys
input = sys.stdin.readline

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

size, min_diff, max_diff = map(int, input().rstrip().split())
land = [list(map(int, input().rstrip().split())) for _ in range(size)]

union_count = 0

while True:
    section = [[False] * size for _ in range(size)]
    union_section = []

    # 영역 분리
    for x in range(size):
        for y in range(size):
            if section[x][y]:
                continue
            section[x][y] = True

            queue = deque([(x, y)])
            union_section.append([])

            while queue:
                curX, curY = queue.popleft()
                union_section[-1].append((curX, curY))

                for i in range(4):
                    nx = curX + dx[i]
                    ny = curY + dy[i]

                    if 0 <= nx < size and 0 <= ny < size and not section[nx][ny]:
                        if min_diff <= abs(land[nx][ny] - land[curX][curY]) <= max_diff:
                            section[nx][ny] = True
                            queue.append((nx, ny))

            if len(union_section[-1]) == 1:
                union_section.pop()

    if len(union_section) == 0:
        break

    # 연합 계산
    for group in union_section:
        total_people = 0
        total_count = len(group)

        for x, y in group:
            total_people += land[x][y]

        distribution_people = total_people // total_count

        for x, y in group:
            land[x][y] = distribution_people         
    union_count += 1   

print(union_count)