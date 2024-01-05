import sys
input = sys.stdin.readline

line, top, length = map(int, input().split())
pascal_sqaure = [[1] * 31 for _ in range(31)]

for i in range(3, 31):
    for j in range(1, i-1):
        pascal_sqaure[i][j] = pascal_sqaure[i-1][j-1] + pascal_sqaure[i-1][j]
    pascal_sqaure[i][i-1] = 1

answer = 0
for i in range(line, line+length):
    for j in range(top-1, top+i-line):
        answer += pascal_sqaure[i][j]

print(answer)