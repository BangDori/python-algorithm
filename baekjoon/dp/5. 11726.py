import sys
input = sys.stdin.readline

size = int(input())
dp = [1 for _ in range(size+1)]

for idx in range(2, size+1):
    dp[idx] = (dp[idx-1] + dp[idx-2]) % 10007
print(dp[-1])