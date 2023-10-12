import sys
input = sys.stdin.readline

def dfs(idx, route):
    for cdx in graph.get(idx):
        if route[cdx] == 1:
            continue

        route[cdx] = 1
        dfs(cdx, route)

row_count = int(input())
rows = []
graph = {}

for row in range(row_count):
    rows.append(list(map(int, input().split())))

for rdx, row in enumerate(rows):
    graph[rdx] = []

    for cdx, col in enumerate(row):
        if col == 1:
            graph[rdx].append(cdx)

for idx in range(row_count):
    route = [0] * row_count
    dfs(idx, route)

    for r in route:
        print(r, end=' ')
    print()