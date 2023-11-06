import sys
input = sys.stdin.readline

N = int(input())
dp = [0, 0, 1, 1]

for i in range(4, N+1):
    next = dp[i-1] + 1
    
    if i % 3 == 0:
        next = min(next, dp[i//3]+1)
    
    if i % 2 == 0:
        next = min(next, dp[i//2]+1)
    
    dp.append(next)

print(dp[N])