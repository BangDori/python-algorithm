import sys
input = sys.stdin.readline

M = int(input())
heights = list(map(int, input().split()))

# 직전 연주 음 < 현재 연주 음 => 직전에 쓴 수보다 큰 수 추가
# 직전 연주 음 > 현재 연주 음 => 직전에 쓴 수보다 작은 수 추가
# 직전 연주 음 = 현재 연주 음 => 직전에 쓴 수 추가

answer = 0
up = down = 0

prev = heights.pop(0)
for current in heights:
    if prev < current:
        down = 0
        up += 1
    elif prev > current:
        down += 1
        up = 0

    answer = max(answer, down, up)
    prev = current

print(answer + 1)