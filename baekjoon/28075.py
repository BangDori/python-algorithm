from itertools import product
import sys
input = sys.stdin.readline

days, min_progress = map(int, input().split())
info_list = list(map(int, input().split()))
monitor_list = list(map(int, input().split()))

progress_list = []
for idx, info, monitor in zip(range(3), info_list, monitor_list):
    progress_list.append((idx, info))
    progress_list.append((idx, monitor))

answer = 0
for progress in product(progress_list, repeat=days):
    tot_score = 0
    last_place = -1

    for place, score in progress:
        if last_place == place:
            tot_score += (score // 2)
        else:
            tot_score += score
        
        last_place = place
    
    if tot_score >= min_progress:
        answer += 1
print(answer)