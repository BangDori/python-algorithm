import sys
input = sys.stdin.readline

cow_count, change_count = map(int, input().split())

quality = list(map(int, input().split()))
quality_sum = [0 for _ in range(cow_count)]

for idx in range(cow_count):
    quality_sum[idx] = quality[idx] * quality[(idx+1)%cow_count] * quality[(idx+2)%cow_count] * quality[(idx+3)%cow_count]

changes = list(map(int, input().split()))

tot_quality_sum = sum(quality_sum)

for change in changes:
    current_sum = 0

    for idx in range(change-4, change):
        change_id = (idx + len(quality_sum)) % len(quality_sum)
        quality_sum[change_id] *= -1

        current_sum += quality_sum[change_id]
    
    tot_quality_sum += current_sum*2 
    print(tot_quality_sum)