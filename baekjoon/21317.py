import sys
input = sys.stdin.readline

rock_count = int(input())
rock_count -= 1

energy = [[0 for _ in range(2)] for _ in range(rock_count)]
for i in range(rock_count):
    low, high = map(int, input().split())
    energy[i][0] = low
    energy[i][1] = high
super_jump = int(input())

dp = [[sys.maxsize for _ in range(2)] for _ in range(rock_count+3)]
dp[0][0] = dp[0][1] = 0
# dp[0][..] # no super jump
# dp[1][..] # use super jump

for i in range(rock_count):
    for k in range(2):
        dp[i+1][k] = min(dp[i+1][k], dp[i][k]+energy[i][0])
        dp[i+2][k] = min(dp[i+2][k], dp[i][k]+energy[i][1])

    dp[i+3][1] = min(dp[i+3][0], dp[i][0]+super_jump)

print(min(dp[rock_count][0], dp[rock_count][1]))