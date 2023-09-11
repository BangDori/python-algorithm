"""
    2 sec, 192 MB

    N(1 <= N <= 100,000)개의 로프
    k개의 로프를 이용하여 중량이 w인 물체를 들어 올릴 때
    각각의 로프에는 모두 고르게 w/k 만큼의 중량
"""

import sys
input = sys.stdin.readline

loop_count = int(input())
max_weights_loop = [int(input()) for _ in range(loop_count)]
max_weights_loop.sort(reverse=True)

answer = 0
for idx in range(len(max_weights_loop)):
    tot_weight = max_weights_loop[idx] * (idx+1)
    if answer < tot_weight:
        answer = tot_weight

print(answer)