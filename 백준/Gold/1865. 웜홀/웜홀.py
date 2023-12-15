import sys
input = sys.stdin.readline

YES = 'YES'
NO = 'NO'

def init(M, W):
    routes = []

    for _ in range(M):
        src, dst, time = map(int, input().split())
        routes.append((src, dst, time)); routes.append((dst, src, time))
        
    for _ in range(W):
        src, dst, time = map(int, input().split())
        routes.append((src, dst, -time))

    return routes

def bf(N):
    times = [10001] * (N+1)
    times[1] = 0

    for i in range(N):
        for route in routes:
            src, dst, time = route

            if times[dst] > times[src] + time:
                times[dst] = times[src] + time

                if i == N-1:
                    return YES
    
    return NO

TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    routes = init(M, W)

    print(bf(N))