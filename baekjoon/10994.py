import sys
input = sys.stdin.readline

num = int(input())
size = (num-1) * 4 + 1
iter_count = (num-1)*2+1

stars = [[' '] * size for _ in range(size)]

for idx in range(0, iter_count+1, 2):
    for row in range(idx, size-idx):
        stars[idx][row] = '*'
        stars[size-1-idx][row] = '*'
        stars[row][idx] = '*'
        stars[row][size-1-idx] = '*'

for row in range(size):
    for col in range(size):
        print(stars[row][col], end='')
    print()