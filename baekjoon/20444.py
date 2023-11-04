import sys
input = sys.stdin.readline

cut_count, paper_count = map(int, input().split())

# row, col
left = 0 # min 0, 4
right = cut_count//2 # max 2, 2

isFind = False
while left <= right:
    mid = (left+right)//2
    mid_count = (cut_count-mid+1) * (mid+1)

    if mid_count == paper_count:
        isFind = True
        break

    if mid_count < paper_count:
        left = mid + 1
    elif mid_count > paper_count:
        right = mid - 1

if isFind:
    print("YES")
else:
    print("NO")