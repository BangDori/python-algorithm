import sys
input = sys.stdin.readline

N = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

left = 0
right = len(liquid)-1
answer = (0, 0, sys.maxsize)

while left < right:
    liquid_sum = liquid[left] + liquid[right]

    if abs(liquid_sum) < answer[2]:
        answer = (left, right, abs(liquid_sum))

        if answer == 0:
            break

    if abs(liquid[left+1]+liquid[right]) > abs(liquid[left] + liquid[right-1]):
        right -= 1
    else:
        left += 1
    
l, r, tot = answer
print(liquid[l], liquid[r])