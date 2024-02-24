import sys
input = sys.stdin.readline

N = int(input())
level = [int(input()) for _ in range(N)]
level.reverse()

answer = 0
for i in range(N-1):
    if level[i] - level[i+1] >= 1:
        continue
    
    answer += (level[i+1] - level[i]) + 1
    level[i+1] = level[i] - 1

print(answer)