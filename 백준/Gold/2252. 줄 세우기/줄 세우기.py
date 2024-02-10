from collections import deque
import sys
input = sys.stdin.readline

people_cnt, compare_cnt = map(int,input().rstrip().split())

graph = [[] for _ in range(people_cnt + 1)]
in_degree = [0 for _ in range(people_cnt + 1)]
queue = deque()

for i in range(compare_cnt):
    pa, pb = map(int,input().rstrip().split())
    graph[pa].append(pb)
    in_degree[pb] += 1

for i in range(1, people_cnt+1):
    if in_degree[i] == 0:
        queue.append(i)

answer = []
while queue:
    person = queue.popleft()
    answer.append(person)

    for np in graph[person]:
        in_degree[np] -= 1
        if in_degree[np] == 0:
            queue.append(np)

print(*answer)