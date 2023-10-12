# 현재 위치 (x, y)
# 왼쪽 아래 (0, 0), 오른쪽 위 (w, h)
x, y, w,h = map(int, input().split())

distance_x = x if (w-x) > x else (w-x)
distance_y = y if (h-y) > y else (h-y)

if distance_x > distance_y:
    print(distance_y)
else:
    print(distance_x)