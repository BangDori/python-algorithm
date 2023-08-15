import sys
input = sys.stdin.readline

# 좌표의 수 (N)
N = int(input())

points_x = list(map(int, input().split()))
pos_x = points_x.copy()
points_dict = {}

points_x = list(set(points_x))
points_x.sort()

for i in range(len(points_x)):
    points_dict[points_x[i]] = i

for i in range(N):
    print(points_dict.get(pos_x[i]), end=' ')
