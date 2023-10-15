import sys
input = sys.stdin.readline

def reverse_row(rows, cols):
    for row in range(rows//2):
        for col in range(cols):
            array[rows-(row+1)][col], array[row][col] = array[row][col], array[rows-(row+1)][col]

def reverse_col(rows, cols):
    for row in range(rows):
        for col in range(cols//2):
            array[row][cols-(col+1)], array[row][col] = array[row][col], array[row][cols-(col+1)]

def rotate_array(rows, cols):
    max_depth = min(rows//2, cols//2)
    rotated_array = [[0 for _ in range(rows)] for _ in range(cols)]

    if rows == cols:
        rotated_array[rows//2][cols//2] = array[rows//2][cols//2]

    for depth in range(max_depth):
        # top -> right
        for col in range(depth, cols-depth):
            rotated_array[col][rows-(depth+1)] = array[depth][col]

        # right -> bottom
        for row in range(depth, rows-depth):
            rotated_array[cols-(depth+1)][row] = array[rows-(row+1)][cols-(depth+1)]

        # bottom -> left
        for col in range(depth, cols-depth):
            rotated_array[cols-(col+1)][depth] = array[rows-(depth+1)][cols-(col+1)]

        # left -> top
        for row in range(depth, rows-depth):
            rotated_array[depth][rows-(row+1)] = array[row][depth]

    return rotated_array

def move_array(rows, cols):
    last = [[0 for _ in range(cols//2)] for _ in range(rows//2)]

    # 4번 그룹 저장
    for row in range(rows//2, rows):
        for col in range(cols//2):
            last[row-rows//2][col] = array[row][col]
    
    # 3 -> 4
    for row in range(rows//2, rows):
        for col in range(cols//2):
            array[row][col] = array[row][col+cols//2]

    # 2 -> 3
    for row in range(rows//2, rows):
        for col in range(cols//2, cols):
            array[row][col] = array[row-rows//2][col]

    # 1 -> 2
    for row in range(rows//2):
        for col in range(cols//2, cols):
            array[row][col] = array[row][col-cols//2]

    # 4 -> 1
    for row in range(rows//2):
        for col in range(cols//2):
            array[row][col] = last[row][col]

rows, cols, op_count = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(rows)]
ops = list(map(int, input().split()))

for op in ops:
    if op == 1:
        # 상하 반전
        reverse_row(rows, cols)
    elif op == 2:
        # 좌우 반전
        reverse_col(rows, cols)
    elif op == 3:
        # → 90도 회전
        array = rotate_array(rows, cols)
        rows, cols = cols, rows
    elif op == 4:
        # 4: ← 90도 회전
        for _ in range(3):
            array = rotate_array(rows, cols)
            rows, cols = cols, rows
    elif op == 5:
        move_array(rows, cols)
    else:   
        for _ in range(3):
            move_array(rows, cols)

for row in range(rows):
    for col in range(cols):
        print(array[row][col], end=' ')
    print()