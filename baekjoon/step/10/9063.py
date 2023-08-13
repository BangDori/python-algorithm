n = int(input())

marble_x = []
marble_y = []

for i in range(n):
    x, y = map(int, input().split()) # 옥구슬의 위치

    marble_x.append(x)
    marble_y.append(y)

marble_x.sort()
marble_y.sort()

distance_x = marble_x[len(marble_x)-1] - marble_x[0]
distance_y = marble_y[len(marble_y)-1] - marble_y[0]

print(distance_x * distance_y)