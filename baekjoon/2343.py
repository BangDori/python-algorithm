import sys
input = sys.stdin.readline

lecture_count, bluelay_answer = map(int, input().split())
lecture_min = list(map(int, input().split()))

left = max(lecture_min)
right = sum(lecture_min)
mid = (left + right) // 2

answer = 0
while left <= right:
    mid = (left + right) // 2

    bluelay_min = 0
    bluelay_count = 0
    for min in lecture_min:
        if bluelay_min < min:
            bluelay_count += 1
            bluelay_min = (mid - min)
            continue

        bluelay_min -= min
    
    if bluelay_count == bluelay_answer:
        answer = mid

    if bluelay_count <= bluelay_answer:
        right = mid - 1
    else:
        left = mid + 1

if answer != 0:
    print(answer)
else:
    print(mid)