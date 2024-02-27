N = int(input())
dp = [0 for _ in range(N+1)]

answer = -1
if N == 1: answer = 3
elif N == 2: answer = 7
else:
    dp[1] = 3
    dp[2] = 7

    for i in range(3, N+1):
        dp[i] = (dp[i-1] * 2 + dp[i-2]) % 9901
    
    answer = dp[N]

print(answer)