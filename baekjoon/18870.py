import sys
input = sys.stdin.readline

N = int(input().strip())
coords = list(map(int, input().split()))
coords_copy = coords.copy()
dict = {}

count = 0
coords_copy.sort()
for coord in coords_copy:
    if dict.get(coord) == None:
        dict[coord] = count
        count += 1

for coord in coords:
    print(dict.get(coord), end=' ')