import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
prefix_sum = [0 for _ in range(N)]
remain = [0 for _ in range(M)]

for i in range(N):
    if i == 0:
        prefix_sum[i] = A[i]
    else:
        prefix_sum[i] = prefix_sum[i-1] + A[i]
    
    remain[prefix_sum[i] % M] += 1

answer = remain[0]
for count in remain:
    answer += (count * (count-1) // 2)
print(answer)