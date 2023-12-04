from itertools import product
import sys
input = sys.stdin.readline

s_nums = [i*i for i in range(1, 225)]
dp = [False for _ in range(50001)]

k = 0
for i in range(1, 50001):
    if i == s_nums[k]:
        dp[i] = True
        k += 1

n = int(input())
answer = 0

if dp[n]:
    answer = 1
else:
    for count in range(4):
        if answer != 0:
            break

        for numbers in product(s_nums, repeat=count):
            if n-sum(numbers) < 0:
                continue
            if dp[n-sum(numbers)]:
                answer = count+1
                break
    
print(4 if answer == 0 else answer)