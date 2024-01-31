from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
belt = deque(list(map(int, input().split())))
robots = deque([0] * N)
answer = 0

while belt.count(0) < K:
    answer += 1

    # 1. 벨트, 로봇 회전
    belt.rotate(1)
    robots.rotate(1)
    robots[-1] = 0

    # 2. 로봇 이동 확인
    if sum(robots): # 로봇이 존재하면
        for i in range(N-2, -1, -1):
            if robots[i] == 0:
                continue

            if robots[i+1] == 0 and belt[i+1] >= 1:
                robots[i] = 0
                robots[i+1] = 1
                belt[i+1] -= 1
        robots[-1] = 0

    # 3. 로봇 X, 내구도 1 이상
    if robots[0] == 0 and belt[0] >= 1:
        robots[0] = 1
        belt[0] -= 1

print(answer)