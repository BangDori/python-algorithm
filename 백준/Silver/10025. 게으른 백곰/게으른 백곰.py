import sys
input = sys.stdin.readline

N, K = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(N)]
ice.sort(key=lambda v: v[1])

curr_sum = 0
start = K

left = 0
right = 0

for i in range(len(ice)):
    if ice[i][1] >= start - K and ice[i][1] <= start + K:
        curr_sum += ice[i][0]
        right = i
    else:
        break

answer = curr_sum
while start <= ice[-1][1]-K:
    start += 1

    while ice[left][1] < start - K:
        curr_sum -= ice[left][0]
        left += 1
    while right+1 < N and ice[right+1][1] <= start + K:
        curr_sum += ice[right+1][0]
        right += 1
    if right >= N:
        right -= 1
    if ice[right][1] > start + K:
        curr_sum -= ice[right][0]
        right -= 1
    
    answer = max(answer, curr_sum)

print(answer)