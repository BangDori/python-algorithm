import sys
input = sys.stdin.readline

def find(child):
    if parent[child] == child: return child
    parent[child] = find(parent[child])
    return find(parent[child])

def union(a, b):
    a, b = find(a), find(b)
    parent[b] = a

room_cnt, warp_cnt = map(int, input().split())
warp = [list(map(int, input().split())) for _ in range(warp_cnt)]
escape = list(map(int, input().split()))
for i, cost in enumerate(escape):
    warp.append([0, i+1, cost])

warp.sort(key=lambda x: x[2])
parent = [i for i in range(room_cnt+1)]

answer = 0

for a, b, warp_time in warp:
    if find(a) != find(b):
        union(a, b)
        answer += warp_time

print(answer)