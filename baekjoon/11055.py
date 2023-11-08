import sys
input = sys.stdin.readline

size = int(input())
array = list(map(int, input().split()))

dp = [[] for _ in range(size)]
dp[0] = [array[0]]

for i in range(1, size):
    for k in range(i):
        temp = []

        if array[i] == dp[k][-1]:
            temp = dp[k]
        elif array[i] > dp[k][-1]:
            temp = dp[k] + [array[i]]
        else:    
            temp = [array[i]]

        dp[i] = temp if sum(dp[i]) < sum(temp) else dp[i]

answer = 0
for temp in dp:
    answer = max(answer, sum(temp))
print(answer)