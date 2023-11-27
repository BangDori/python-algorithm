import sys
input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))

dp = [-1001 for _ in range(N)]
dp[0] = array[0]

for i in range(1, N):
    dp[i] = max(array[i], dp[i-1] + array[i])

print(max(dp))