import sys
input = sys.stdin.readline

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

points.sort(key= lambda point: (point[0], point[1]))

for x, y in points:
    print(x, y)
