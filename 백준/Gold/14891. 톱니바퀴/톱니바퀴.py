from collections import deque
import sys
input = sys.stdin.readline

S = 1
N = 0

gear = [deque(list(map(int, input().strip()))) for _ in range(4)]
rotate_count = int(input())

def rotate(gid, dir):
    if visited[gid]:
        return
    visited[gid] = True

    if gid-1 >= 0 and gear[gid-1][2] != gear[gid][6]:
        rotate(gid-1, dir * -1)

    if gid+1 <= 3 and gear[gid+1][6] != gear[gid][2]:
        rotate(gid+1, dir * -1)

    gear[gid].rotate(dir)

for _ in range(rotate_count):
    gid, dir = map(int, input().split())

    visited = [False for _ in range(4)]
    rotate(gid-1, dir)

answer = 0
for i in range(4):
    answer += ((2 ** i) * gear[i][0])

print(answer)