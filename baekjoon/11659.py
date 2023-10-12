"""
    1 sec, 256 MB

    N 개가 주어졌을 때, i ~ j번째 수까지의 합

    수의 개수 N, 합 횟수 M
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = [0] + list(map(int, input().split()))
sums = [0]

for idx in range(1, len(nums)):
    sums.append(sums[idx-1] + nums[idx])

for _ in range(M):
    i, j = map(int, input().split())
    print(sums[j]-sums[i-1])