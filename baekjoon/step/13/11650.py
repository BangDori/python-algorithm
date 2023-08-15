# 점의 개수 (N)
N = int(input())
points = ['' for _ in range(N)]

for i in range(N):
    x, y = map(int, input().split())
    
    points[i] = x, y
points.sort()

for i in range(N):
    print(points[i][0], points[i][1])
