import sys
input = sys.stdin.readline

N, M = map(int, input().split())
people = [int(input()) for _ in range(N)]
visited = [False for _ in range(N)]
answer = 0

curr = 0
while True:
    if visited[curr]:
        answer = -1
        break

    visited[curr] = True
    answer += 1
    next = people[curr]
 
    if people[curr] == people[next] and people[curr] != M:
        answer = -1
        break
    
    if next == M:
        break

    curr = next

print(answer)