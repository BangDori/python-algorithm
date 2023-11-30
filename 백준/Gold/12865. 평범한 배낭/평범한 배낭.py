import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[0] * (K+1) for _ in range(N+1)]

weights = [0] + []
values = [0] + []
for _ in range(N):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

for i in range(N+1):
    for j in range(K+1):
        if j >= weights[i]:
            dp[i][j] = max(dp[i-1][j], values[i] + dp[i-1][j-weights[i]])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])