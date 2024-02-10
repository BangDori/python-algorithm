from collections import deque
import sys
input = sys.stdin.readline

TC = int(input())
answer = []
for _ in range(TC):
    v, e = map(int, input().split())

    costs = [0]+list(map(int, input().split()))
    graph = [[] for _ in range(v+1)]
    in_degree = [0 for _ in range(v+1)]
    for _ in range(e):
        src, dst = map(int, input().split())

        in_degree[dst] += 1
        graph[src].append(dst)
    find = int(input())

    queue = deque([])
    for i in range(1, v+1):
        if in_degree[i] == 0: queue.append((i, costs[i]))    
    visited = [costs[i] for i in range(v+1)]

    while queue:
        src, cost = queue.popleft()

        if visited[src] > cost: continue

        for dst in graph[src]:
            in_degree[dst] -= 1
            next_cost = cost + costs[dst]

            if next_cost > visited[dst]:
                visited[dst] = next_cost
            if in_degree[dst] == 0:
                queue.append((dst, visited[dst]))

    print(visited[find])