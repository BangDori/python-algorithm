import sys
input = sys.stdin.readline

n = int(input())
friends = [list(input().strip()) for _ in range(n)]

count = [[0] * n for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j: continue

            if friends[i][j] == 'Y' or (friends[i][k] == 'Y' and friends[k][j] == 'Y'):
                count[i][j] = 1

answer = 0
for line in count:
    answer = max(answer, sum(line))
print(answer)