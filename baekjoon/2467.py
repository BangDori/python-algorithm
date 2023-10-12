import sys
input = sys.stdin.readline

N = int(input())
liquid = list(map(int, input().split()))

left = 0
right = N-1

answer = sys.maxsize
answer_left = 0
answer_right = 0

while left < right:
    mixed = abs(liquid[left] + liquid[right])

    if mixed <= answer:
        answer = mixed
        answer_left = liquid[left]
        answer_right = liquid[right] 
    
    moved_left = abs(liquid[left+1] + liquid[right])
    moved_right = abs(liquid[left] + liquid[right-1])

    if moved_left > moved_right:
        right -= 1
    else:
        left += 1

print(answer_left, answer_right)