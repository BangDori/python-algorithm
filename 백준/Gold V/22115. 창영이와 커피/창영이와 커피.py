import sys
input = sys.stdin.readline

n, k = map(int, input().split())
c = [0] + list(map(int, input().split()))

# dp[i][j] = i번 까지 커피, 카페인 양이 j인 커피 최소 개수 저장
dp = [[1e9] * (k+1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][0] = 0

for i in range(1, n+1):
    for j in range(1, k+1):
        if j < c[i]: dp[i][j] = dp[i-1][j]
        else: dp[i][j] = min(dp[i-1][j], dp[i-1][j-c[i]] + 1)

print(dp[n][k] if dp[n][k] != 1e9 else -1)