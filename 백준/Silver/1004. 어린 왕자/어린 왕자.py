import sys, math
input = sys.stdin.readline

def get_distance(x1, y1, x2, y2):
    diff_x = x1 - x2
    diff_y = y1 - y2

    return math.sqrt(diff_x ** 2 + diff_y ** 2)

TC = int(input())
for _ in range(TC):
    sx, sy, ex, ey = map(int, input().split())
    planet_count = int(input())
    planets, distances = [], []

    for i in range(planet_count):
        px, py, pr = map(int, input().split())

        distance_start_point = get_distance(sx, sy, px, py)
        distance_end_point = get_distance(ex, ey, px, py)

        if distance_start_point <= pr or distance_end_point <= pr:
            planets.append((px, py, pr))
            distances.append(distance_start_point)
    
    count = 0
    for i, planet in enumerate(planets):
        px, py, pr = planet
        distance = get_distance(px, py, ex, ey)

        if distances[i] <= pr:
            if distance > pr: count += 1
        else:
            if distance <= pr: count += 1
    
    print(count)