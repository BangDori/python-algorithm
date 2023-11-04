import sys
input = sys.stdin.readline

quiz_count = int(input())
for _ in range(quiz_count):
    a, d, x = map(int, input().split())

    left = 0
    right = x
    while left <= right:
        mid = (left+right)//2

        current_floor = a*mid + mid*(mid-1)*d//2
        before_floor = a*(mid-1) + (mid-1)*(mid-2)*d//2

        if before_floor < x <= current_floor:
            break

        if x > current_floor:
            left = mid+1
        elif x < current_floor:
            right = mid-1
        
    print(mid, x - before_floor)