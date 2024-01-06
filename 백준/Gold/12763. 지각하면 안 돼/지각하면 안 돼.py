import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

building_count = int(input())
limit_time, limit_money = map(int, input().split())

load_count = int(input())
load_info = [[] for _ in range(101)]

for _ in range(load_count):
    src, dst, time, taxi = map(int, input().split())

    load_info[src].append((dst, time, taxi))
    load_info[dst].append((src, time, taxi))

answer = float('inf')

# 시간, 돈
# visited = [(limit_time, limit_money+1) for _ in range(building_count+1)]
def dfs(pos, time, money):
    global answer
    if pos == building_count:
        answer = min(answer, money)
        return

    for dst, need_time, need_money in load_info[pos]:
        if time + need_time > limit_time or money + need_money > limit_money:
            continue

        # if visited[dst][1] > money + need_money:
        #     visited[dst] = (time + need_time, money + need_money)
        dfs(dst, time + need_time, money + need_money)
    
dfs(1, 0, 0)
print(-1 if answer == float('inf') else answer)