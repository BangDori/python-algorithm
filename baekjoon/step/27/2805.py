"""
    1 sec, 256 MB
    
    나무 M미터 필요

    절단기를 이용해 나무를 절단.
    절다기에 높이 H 지정

    ex) 20 15 10 17 일 때, H = 15
        => 15 15 10 15, 5 + 2 = 7M 나무를 집에 들고 감

    M미터의 나무를 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값

    입력
    1. 나무의 수 N, 나무의 길이 M (1 <= N <= 1,000,000, 1 <= M <= 2,000,000,000)
    2. 나무의 높이들 H (0 <= H < 1,000,000,000)
"""

import sys
input = sys.stdin.readline

answer = -1
count, length = map(int,input().split())
heights = list(map(int, input().split()))

min_height = 0
max_height = max(heights)

lengths = []
while min_height <= max_height:
    cut_height = (min_height + max_height) // 2
    # print(min_height, cut_height, max_height)

    cur_length = 0
    for height in heights:
        if cut_height < height:
            cur_length += (height - cut_height)
    
    # print("[INFO]", cur_length, cut_height)
    
    if length == cur_length:
        answer = cut_height
        break
    elif length < cur_length:
        min_height = cut_height + 1
        lengths.append(cut_height)
    else:
        max_height = cut_height - 1

if answer != -1:
    print(answer)
else:
    print(lengths[-1])