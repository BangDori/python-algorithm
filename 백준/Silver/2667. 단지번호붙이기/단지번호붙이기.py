import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
matrix = [list(map(int, input().rstrip())) for _ in range(N)]
section = [[0 if matrix[row][col] == 0 else -1 for col in range(N)] for row in range(N)]

section_num = 0
section_count_list = []

def dfs(row, col):
    global section_count

    section_count += 1
    for i in range(4):
        nrow = row + dx[i]
        ncol = col + dy[i]

        if 0 <= nrow < N and 0 <= ncol < N and section[nrow][ncol] == -1:
            section[nrow][ncol] = section_num
            dfs(nrow, ncol)

for row in range(N):
    for col in range(N):
        if section[row][col] == -1:
            section_num += 1
            section[row][col] = section_num

            section_count = 0
            dfs(row, col)

            section_count_list.append(section_count)

print(section_num)
section_count_list.sort()
for section_count in section_count_list:
    print(section_count)