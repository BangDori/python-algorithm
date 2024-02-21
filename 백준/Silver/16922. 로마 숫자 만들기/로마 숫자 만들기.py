import sys
sys.setrecursionlimit(10 ** 2)
input = sys.stdin.readline

N = int(input())

visited = [[False] * 1001 for _ in range(N+1)]
answer = 0

def dfs(num, cnt):
    global answer
    if cnt == N:
        answer += 1
        return
    
    if not visited[cnt+1][num+1]:
        visited[cnt+1][num+1] = True
        dfs(num+1, cnt+1)
    
    if not visited[cnt+1][num+5]:
        visited[cnt+1][num + 5] = True
        dfs(num+5, cnt+1)

    if not visited[cnt+1][num+10]:
        visited[cnt+1][num+10] = True
        dfs(num+10, cnt+1)

    if not visited[cnt+1][num+50]:
        visited[cnt+1][num+50] = True
        dfs(num+50, cnt+1)

dfs(0, 0)

print(answer)