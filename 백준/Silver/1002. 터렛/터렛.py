import sys, math
input = sys.stdin.readline

def get_distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

TC = int(input())
for _ in range(TC):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    distance = get_distance(x1, y1, x2, y2)

    count = 0
    if (x1, y1, r1) == (x2, y2, r2):
        count = -1
    elif abs(r1 - r2) == distance or r1 + r2 == distance:
        count = 1
    elif abs(r1 - r2) < distance < r1 + r2:
        count = 2
    else:
        count = 0

    print(count)