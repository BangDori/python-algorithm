"""
    2 sec, 128 MB

    K개의 랜석을 가지고 있음 (길이 제각각)
    N개의 같은 길이의 랜선으로 만들기
"""

import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lines = []
for _ in range(K):
    lines.append(int(input()))

min = 1
max = max(lines)

answer = 0
lengths = []
while min <= max:
    mid = (min + max) // 2

    tot_lines = 0
    for line in lines:
        tot_lines += line // mid
    
    if tot_lines >= N:
        min = mid + 1
        answer = mid
    else:
        max = mid - 1
    
print(answer)