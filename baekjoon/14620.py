from itertools import combinations 
import sys
input = sys.stdin.readline

size = int(input())
matrix = [list(map(int, input().split())) for _ in range(size)]

flowerA = []
flowerB = []
flowerC = []
answer = 0

# (1, 1) ~ (size-2, szie-2) 3개

flower_list = []
for i in range(1, size-1):
    for j in range(1, size-1):
        flower_list.append((i, j))

def disable_location(locations):
    [a, b, c] = locations

    if abs(a[0] - b[0]) + abs(a[1] - b[1]) <= 2:
        return True
        
    if abs(b[0] - c[0]) + abs(b[1] - c[1]) <= 2:
        return True
    
    if abs(c[0] - a[0]) + abs(c[1] - a[1]) <= 2:
        return True
    
    return False

dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, 1, -1]

def get_cost(locations):
    cost = 0

    for location in locations:
        x, y = location

        for i in range(5):
            nx = x + dx[i]
            ny = y + dy[i]

            cost += matrix[nx][ny]
        
    return cost

answer = sys.maxsize
for locations in combinations(flower_list, 3):
    if disable_location(locations):
        continue
    
    cost = get_cost(locations)
    if answer > cost:
        answer = cost

print(answer)