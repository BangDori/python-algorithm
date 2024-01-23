import sys
input = sys.stdin.readline

fruit = int(input())
field = [list(map(int, input().split())) for _ in range(6)]

max_w, max_h = 0, 0
max_w_idx, max_h_idx = 0, 0

for idx, info in enumerate(field):
    dir, length = info

    if dir == 1 or dir == 2:
        if length > max_w:
            max_w = length
            max_w_idx = idx
    else:
        if length > max_h:
            max_h = length
            max_h_idx = idx

min_w, min_h = 0, 0

if field[(max_w_idx+1)%6][1] > field[max_w_idx-1][1]:
    min_w = field[max_w_idx-2][1]
    min_h = field[max_w_idx-3][1]
else:
    min_w = field[(max_w_idx+2) % 6][1]
    min_h = field[(max_w_idx+3) % 6][1]

total_field = (max_w*max_h) - (min_w*min_h)
answer = total_field * fruit

print(answer)