def getTime(array, height, block):
    time = 0

    for cur_height in array:
        diff = cur_height - height

        if diff > 0:
            # 블록 제거 (2s)
            time = time + diff * 2
            block = block + diff
        else:
            # 블록 놓기 (1s)
            time = time + abs(diff)
            block = block - abs(diff)
    
    if block < 0:
        return -1
    
    return time

import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())

# 땅
array = []
for _ in range(N):
    array += list(map(int, input().split()))

# 범위 (최소 높이 ~ 최대 높이)
min_height = min(array)
max_height = max(array)

answer_time = sys.maxsize
answer_height = -1

for height in range(min_height, max_height+1):
    current_block = B
    current_time = getTime(array, height, current_block)

    if current_time == -1:
        continue

    if current_time <= answer_time and height > answer_height:
        answer_time = current_time
        answer_height = height

print(answer_time, answer_height)