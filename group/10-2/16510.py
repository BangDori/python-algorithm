import sys
input = sys.stdin.readline

def binary_search(time):
    left = 0
    right = len(sums)-1
    mid = (left+right)//2

    while left <= right:
        mid = (left+right)//2

        if sums[mid] <= time < sums[mid+1]:
            return mid
        elif sums[mid] > time:
            right = mid-1
        else:
            left = mid+1
    
    return mid

work_count, hour_count = map(int, input().split())
work = list(map(int, input().split()))

sums = [0 for _ in range(work_count)]
sums[0] = work[0]

for idx in range(1, len(work)):
    sums[idx] = sums[idx-1] + work[idx]

for _ in range(hour_count):
    hour = int(input())

    work_on_hour = 0
    if hour >= sums[-1]:
        work_on_hour = work_count
    elif hour < sums[0]:
        work_on_hour = 0
    else:
        work_on_hour = binary_search(hour)+1

    print(work_on_hour)