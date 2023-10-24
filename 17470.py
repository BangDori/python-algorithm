# Wrong Answer

import sys
input = sys.stdin.readline

rows, cols, op_count = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(rows)]
new_matrix = [[matrix[row][col] for col in range(cols)] for row in range(rows)]

def reverse_top_down():
    size = rows // 2

    for i in range(size):
        temp = matrix[i]
        matrix[i] = matrix[-(i+1)]
        matrix[-(i+1)] = temp

def reverse_left_right():
    for i in range(rows):
        matrix[i].reverse()

def rotate_right():
    global matrix, new_matrix

    new_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

    for col in range(cols):
        for row in range(rows):
            new_matrix[col][row] = matrix[row][col]
        new_matrix[col].reverse()

    matrix = [[0 for _ in range(rows)] for _ in range(cols)]

    for col in range(cols):
        for row in range(rows):
            matrix[col][row] = new_matrix[col][row]

def rotate_left():
    global matrix, new_matrix
    new_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

    for col in range(cols):
        for row in range(rows):
            new_matrix[col][row] = matrix[row][col]
    
    matrix = [[0 for _ in range(rows)] for _ in range(cols)]

    for col in range(cols):
        for row in range(rows):
            matrix[col][row] = new_matrix[col][row]

def move_group_right():
    # 1 (0, 0) ~ (rows//2, cols//2)
    for row in range(rows//2):
        for col in range(cols//2):
            new_matrix[row][col] = matrix[rows//2+row][col]

    # 2 (0, cols//2) ~ (rows//2, cols)
    for row in range(rows//2):
        for col in range(cols//2, cols):
            new_matrix[row][col] = matrix[row][col-cols//2]

    # 3 (rows//2, cols//2) ~ (rows, cols)
    for row in range(rows//2, rows):
        for col in range(cols//2, cols):
            new_matrix[row][col] = matrix[row-rows//2][col]

    # 4 (rows//2, 0) ~ (rows, cols//2)
    for row in range(rows//2, rows):
        for col in range(cols//2):
            new_matrix[row][col] = matrix[row][col+cols//2]

    sync_moved_matrix()

def move_group_left():
    # 1 (0, 0) ~ (rows//2, cols//2)
    for row in range(rows//2):
        for col in range(cols//2):
            new_matrix[row][col] = matrix[row][col+cols//2]

    # 2 (0, cols//2) ~ (rows//2, cols)
    for row in range(rows//2):
        for col in range(cols//2, cols):
            new_matrix[row][col] = matrix[row+rows//2][col]

    # 3 (rows//2, cols//2) ~ (rows, cols)
    for row in range(rows//2, rows):
        for col in range(cols//2, cols):
            new_matrix[row][col] = matrix[row][col-cols//2]

    # 4 (rows//2, 0) ~ (rows, cols//2)
    for row in range(rows//2, rows):
        for col in range(cols//2):
            new_matrix[row][col] = matrix[row-rows//2][col]

    sync_moved_matrix()

def sync_moved_matrix():
    for row in range(rows):
        for col in range(cols):
            matrix[row][col] = new_matrix[row][col]

ops = list(map(int, input().rstrip().split()))

prev = ops[0]
count = 1

new_ops = []
for i in range(1, len(ops)):
    if prev == ops[i]:
        count += 1
    else:
        new_ops.append((prev, count))
        prev = ops[i]
        count = 1
new_ops.append((prev, count))

i = 0
while i < len(new_ops)-1:
    if (new_ops[i][0] in [3,4] and new_ops[i+1][0] in [3, 4]) or (new_ops[i][0] in [5, 6] and new_ops[i+1][0] in [5, 6]):
        diff = new_ops[i][1] - new_ops[i+1][1]

        new_ops[i] = (new_ops[i][0], diff)
        new_ops[i+1] = (new_ops[i+1][0], diff)
        i += 2
        continue

    i += 1

ops.clear()
for op, count in new_ops:
    if count < 0:
        continue

    if op == 1:
        ops += [1] * (count % 2)
    elif op == 2:
        ops += [2] * (count % 2)
    elif op == 3:
        ops += [3] * (count % 4)
    elif op == 4:
        ops += [4] * (count % 4)
    elif op == 5:
        ops += [5] * (count % 4)
    else:
        ops += [6] * (count % 4)

for op in ops:
    if op == 1:
        reverse_top_down()
    elif op == 2:
        reverse_left_right()
    elif op == 3:
        rotate_right()
        rows, cols = cols, rows
    elif op == 4:
        rotate_left()
        rows, cols = cols, rows
        reverse_top_down()
    elif op == 5:
        move_group_right()
    elif op == 6:
        move_group_left()

for row in range(rows):
    for col in range(cols):
        print(matrix[row][col], end=' ')
    print()