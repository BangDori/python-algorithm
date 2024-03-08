# 17179 - 케이크 자르기

import sys
input = sys.stdin.readline

def is_minimum(mid, cut_count):
    left = 0
    cnt = 0

    for right in cut_points:
        if right - left >= mid:
            left = right
            cnt += 1

    return cnt > cut_count

N, M, L = map(int, input().split())
cut_points = [int(input()) for _ in range(M)] + [L]

for _ in range(N):
    cut_count = int(input())

    left, right = 1, L
    answer = 0

    while left <= right:
        mid = (left + right) // 2

        if is_minimum(mid, cut_count):
            left = mid + 1
            answer = max(mid, answer)
        else:
            right = mid - 1

    print(answer)