import sys
input = sys.stdin.readline

dp = [1 for _ in range(1001)]

N, K = map(int, input().split())

if K > N // 2 + 1:
    K = N - K

division = 1
for idx in range(1, K+1):
    dp[idx] = dp[idx-1] * (N-idx+1)
    division *= idx

print((dp[K]//division) % 10007)