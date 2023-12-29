# ## 2

# import sys
# input = sys.stdin.readline

# word = input().rstrip()
# wolf_order_dict = { 'w': 0, 'o': 1, 'l': 2, 'f': 3 }
# wolf_count = [0, 0, 0, 0]

# isWrong = False
# for alpha in word:
#     order = wolf_order_dict[alpha]
#     wolf_count[order] += 1

#     for i in range(1, order):
#         if wolf_count[i] != wolf_count[i-1]:
#             isWrong = True

#     if isWrong:
#         break

# # 최종 점검
# for i in range(1, len(wolf_count)):
#     if wolf_count[i-1] != wolf_count[i]:
#         isWrong = True

# if len(word) == 0:
#     print(0)
# else:
#     print(0 if isWrong else 1)

from collections import deque
import sys
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

row, col, limit_time = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(row)]

visited = [[[False] * col for _ in range(row)] for _ in range(2)]
# row, col, time, sword
queue = deque([(0, 0, 0, 0)])
answer = sys.maxsize
isSuccess = False

while queue:
    cur_r, cur_c, time, sword = queue.popleft()

    if cur_r == row-1 and cur_c == col-1 and time <= limit_time:
        answer = min(answer, time)
        isSuccess = True

    for i in range(4):
        nr = cur_r + dr[i]
        nc = cur_c + dc[i]

        if 0 <= nr < row and 0 <= nc < col and not visited[sword][nr][nc]:
            visited[sword][nr][nc] = True

            if matrix[nr][nc] == 2 or (matrix[nr][nc] == 1 and sword == 1):
                queue.append((nr, nc, time+1, 1))
            if matrix[nr][nc] == 0:
                queue.append((nr, nc, time+1, sword))

print(answer if isSuccess else 'Fail')