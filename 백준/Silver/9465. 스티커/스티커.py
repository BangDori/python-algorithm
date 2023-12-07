import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0 for _ in range(n)] for _ in range(2)]

    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]

    if n >= 2:
        dp[0][1] = stickers[0][1] + dp[1][0]
        dp[1][1] = stickers[1][1] + dp[0][0]

        for i in range(2, n):
            for k in range(2):
                dp[k][i] = max(stickers[k][i] + dp[(k+1)%2][i-1], stickers[k][i] + dp[(k+1)%2][i-2])
    
    print(max(dp[0][-1], dp[1][-1]))