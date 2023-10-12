import sys
input = sys.stdin.readline

def rotate_array(array, rows, cols, max_depth):
    for depth in range(max_depth):
        isOne = True
        temp = array[depth][depth]

        # ←
        for col in range(depth, cols-depth-1):
            isOne = False
            array[depth][col] = array[depth][col+1]

        # ↑
        for row in range(depth, rows-depth-1):
            isOne = False
            array[row][(cols-1)-depth] = array[row+1][(cols-1)-depth]

        # →
        for col in range(depth, cols-depth-1):
            isOne = False
            array[(rows-1)-depth][(cols-1)-col] = array[(rows-1)-depth][(cols-1)-col-1]

        # ↓
        for row in range(depth, rows-depth-1):
            isOne = False
            array[(rows-1)-row][depth] = array[(rows-1)-row-1][depth]

        if not isOne:
            array[depth+1][depth] = temp

rows, cols, rotate = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(rows)]

layer = min(rows//2 + rows%2, cols//2 + cols%2)

for _ in range(rotate):
    rotate_array(array, rows, cols, layer)

for row in range(rows):
    for col in range(cols):
        print(array[row][col], end=' ')
    print()