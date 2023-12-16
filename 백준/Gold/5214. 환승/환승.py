from collections import deque
import sys
input = sys.stdin.readline

vertex, edge, hyper = map(int, input().split())
graph = [[] for _ in range(vertex+1)]
hyper_tube = [[] for _ in range(hyper+1)]

for i in range(1, hyper+1):
    network = list(map(int, input().split()))
    hyper_tube[i] = network

    for station in network:
        graph[station].append(i)

def bfs(start):
    queue = deque([(1, start)])
    visited_station = [False for _ in range(vertex+1)]
    visited_hyper = [False for _ in range(hyper+1)]
 
    while queue:
        count, src = queue.popleft()

        if src == vertex:
            return count
        
        for tube in graph[src]:
            if visited_hyper[tube]:
                continue
            visited_hyper[tube] = True

            for dst in hyper_tube[tube]:
                if dst == vertex:
                    return count+1

                if not visited_station[dst] and dst != src:
                    visited_station[dst] = True
                    queue.append((count+1, dst))
    
    return -1
    
print(bfs(1))