import sys
input = sys.stdin.readline

INCREMENT = 0
DECREAMENT = 1

N = int(input())
A = list(map(int, input().split()))


if N == 1:
    print(1)
else:
    dp = [[0] * 2 for _ in range(N)]
    # dp[0] 증가하는 부분
    # dp[1] 감소하는 부분
    dp[0][0] = 1; dp[1][0] = 0

    def fill_dp(mode):
        for next in range(1, N):
            next_value = 1 if mode == INCREMENT else 0

            for prev in range(next):
                if A[prev] < A[next]:
                    next_value = max(next_value, dp[prev][mode]+1)

            dp[next][mode] = next_value

    fill_dp(INCREMENT)
    A.reverse()
    fill_dp(DECREAMENT)

    answer = 0
    for i in range(N):
        answer = max(answer, dp[i][0] + dp[-(i+1)][1])

    print(answer)