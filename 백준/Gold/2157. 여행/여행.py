import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
airport=[[0] * (N+1) for _ in range(N+1)]

for _ in range(K):
    src, dst, score = map(int, input().split())
    airport[src][dst] = max(airport[src][dst], score)

# 위치 + 횟수
dp = [[0] * M for _ in range(N+1)]

for i in range(N+1):
    dp[i][1] = airport[1][i]

for src in range(1, N+1):
    for dst in range(src+1, N+1):
        if airport[src][dst] == 0:
            continue

        for pos in range(M-1):
            if dp[src][pos] == 0:
                continue

            dp[dst][pos+1] = max(dp[dst][pos+1], airport[src][dst] + dp[src][pos])

print(max(dp[N]))