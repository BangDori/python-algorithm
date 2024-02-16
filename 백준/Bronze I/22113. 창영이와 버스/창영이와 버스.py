import sys
input = sys.stdin.readline

# N개의 버스
# S 버스 -> E 버스 환승 비용: A(SE)

N, M = map(int, input().split())
use_bus = list(map(int, input().split()))
table = [list(map(int, input().split())) for _ in range(N)]

answer = 0
for i in range(1, len(use_bus)):
    answer += table[use_bus[i-1]-1][use_bus[i]-1]

print(answer)