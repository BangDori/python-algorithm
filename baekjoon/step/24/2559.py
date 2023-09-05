"""
    1 sec, 128 MB

    연속적인 며칠 동안의 온도의 합이 가장 큰지

    입력
        N (온도를 측정한 전체 날짜의 수), K (합을 구하기 위한 연속적인 날짜의 수)
        온도를 나타내는 N개의 정수
"""

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
temps = list(map(int, input().split()))
sums = [0]

for idx in range(N):
    sums.append(sums[idx] + temps[idx])

max_temp = -sys.maxsize

if N == K:
    max_temp = sum(temps)
else:
    for idx in range(len(sums)):
        if len(sums) <= idx+K:
            break

        if sums[idx+K] - sums[idx] > max_temp:
            max_temp = sums[idx+K] - sums[idx]

print(max_temp)