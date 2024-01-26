import sys
input = sys.stdin.readline

N = int(input()) # 사람의 수
N_list = list(map(int, input().split()))
result = []

pos = N-1
height = N
for i in range(N):
    result.insert(N_list[pos], height)
    pos -= 1; height -= 1

print(*result)