from bisect import bisect_right
import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
X = int(input())

numbers.sort()
l = 0; r = min(bisect_right(numbers, X-1), len(numbers)-1)

answer = 0
while l < r:
    s = numbers[l] + numbers[r]
    if s == X:
        answer += 1
    
    if s < X:
        l += 1
    elif s > X:
        r -= 1
    else:
        if numbers[l+1] + numbers[r] == X:
            l += 1
        else:
            r -= 1

print(answer)