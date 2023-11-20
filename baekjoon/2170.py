from collections import deque
import sys
input = sys.stdin.readline

def solution(points):
    points.sort(key=lambda v: (v[0], v[1]))
    queue = deque(points)

    answer = 0
    x, y = queue.popleft()
    while queue:
        x2, y2 = queue.popleft()

        if x2 >= x and x2 <= y:
            if y2 > y:
                y = y2
            continue
        
        answer += (y-x)
        x, y = x2, y2

    answer += (y-x)
    
    print(answer)

N = int(input())
points = []

for _ in range(N):
    start, end = map(int, input().split())
    points.append((start, end))

solution(points)