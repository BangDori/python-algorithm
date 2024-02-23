import sys
sys.setrecursionlimit(10 ** 6)

def dfs(pid):
    global result

    visited[pid] = True
    team.append(pid)
    next_pid = people[pid]
    
    if visited[next_pid]:
        if next_pid in team:
            result += team[team.index(next_pid):]
        return

    dfs(next_pid)

TC = int(input())

for _ in range(TC):
    N = int(input())
    
    people = [0] + list(map(int, input().split()))
    visited = [True] + [False for _ in range(N)]
    result = []
    
    for pid in range(1, N+1):
        if not visited[pid]:
            team = []
            dfs(pid)
            
    print(N - len(result))