import sys
input = sys.stdin.readline

row, col = map(int, input().split())
origin_image = [list(input()) for _ in range(row)]
converted_image = [['.' for _ in range(col)] for _ in range(row)]

meteo = [(0, 0) for _ in range(col)]
ground = [(0, 0) for _ in range(col)]

for r in range(row):
    for c in range(col):
        if origin_image[r][c] == '.':
            continue

        if origin_image[r][c] == 'X':
            meteo[c] = (r+1, c)
            continue

        if origin_image[r][c] == '#' and ground[c] == (0, 0):
            ground[c] = (r, c)

min_diff = sys.maxsize
for idx in range(col):
    if meteo[idx][0] == 0:
        continue

    cur_diff = ground[idx][0] - meteo[idx][0]
    if min_diff > cur_diff:
        min_diff = cur_diff

for r in range(row):
    for c in range(col):
        if origin_image[r][c] == '.':
            continue

        if origin_image[r][c] == '#':
            converted_image[r][c] = '#'
            continue

        converted_image[r+min_diff][c] = origin_image[r][c]

for r in range(row):
    for c in range(col):
        sys.stdout.write(converted_image[r][c])
    sys.stdout.write('\n')