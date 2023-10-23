from itertools import permutations
from collections import deque
import sys
input = sys.stdin.readline

x, y, rotate_count = map(int, input().split())
origin = [list(map(int, input().split())) for _ in range(x)]
rotate_list = []

for _ in range(rotate_count):
    r, c, s = map(int, input().split())
    rotate_list.append((r-1, c-1, s))

def rotate(r, c, s):
    start_x = r-s
    start_y = c-s

    end_x = r+s
    end_y = c+s

    for depth in range(s):
        initial_list = deque([])

        for cur_y in range(start_y+depth, end_y-depth):
            initial_list.append(matrix[start_x+depth][cur_y])
                
        for cur_x in range(start_x+depth, end_x-depth):
            initial_list.append(matrix[cur_x][end_y-depth])

        reverse_list = []
        for cur_y in range(start_y+depth, end_y-depth):
            reverse_list.append(matrix[end_x-depth][cur_y+1])

        reverse_list.reverse()
        initial_list += reverse_list
        reverse_list.clear()

        for cur_x in range(start_x+depth, end_x-depth):
            reverse_list.append(matrix[cur_x+1][start_y+depth])
        
        reverse_list.reverse()
        initial_list += reverse_list

        initial_list.appendleft(initial_list.pop())

        for cur_y in range(start_y+depth, end_y-depth):
            matrix[start_x+depth][cur_y] = initial_list.popleft()
        
        for cur_x in range(start_x+depth, end_x-depth):
            matrix[cur_x][end_y-depth] = initial_list.popleft()
        
        for cur_y in range(end_y-depth, start_y+depth, -1):
            matrix[end_x-depth][cur_y] = initial_list.popleft()

        for cur_x in range(end_x-depth, start_x+depth, -1):
            matrix[cur_x][start_y+depth] = initial_list.popleft()

answer = sys.maxsize
for perm in permutations(rotate_list, len(rotate_list)):
    matrix = [[origin[i][j] for j in range(y)] for i in range(x)]
    for r_info in perm:
        rotate(r_info[0], r_info[1], r_info[2])

    for matrix_row in matrix:
        if answer > sum(matrix_row):
            answer = sum(matrix_row)
print(answer)