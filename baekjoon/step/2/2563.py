paper = [[0 for _ in range(100)] for _ in range(100)]
area = 0
count = int(input())

for _ in range(count):
    x, y = map(int, input().split())

    for i in range(y, y+10):
        for j in range(x, x+10):
            paper[j][i] = 1

for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            area += 1

print(area)