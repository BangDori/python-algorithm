import sys
input = sys.stdin.readline

N, K = map(int, input().split())
block_dist = list(map(int, input().split()))

l = 0; r = 0
jump_cnt = 0

answer = 0
while r < N-1:
    # 이동 거리 범위 이내라면
    if block_dist[r] <= K:
        r += 1
        continue

    if block_dist[r] > K and jump_cnt == 0:
        jump_cnt += 1
        r += 1
        continue

    if block_dist[r] > K:
        if block_dist[l] > K:
            jump_cnt -= 1
        answer = max(answer, r-l+1)

        l += 1

answer = max(answer, r-l+1)
print(answer)