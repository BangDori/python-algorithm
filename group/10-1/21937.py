import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

work_count, work_order_count = map(int, input().split())

work_dict = {}
visited = [False] * (work_count+1)
for idx in range(work_count):
    work_dict[idx+1] = []

for _ in range(work_order_count):
    prev, next = map(int, input().split())
    work_dict[next].append(prev)

find = int(input())

answer = 0
def dfs(find):
    global answer
    find_list = work_dict.get(find)

    visited[find] = True

    for f in find_list:
        if not visited[f]:
            answer += 1
            dfs(f)

dfs(find)
print(answer)