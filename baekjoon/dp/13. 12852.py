import sys
input = sys.stdin.readline

X = int(input())
dp = [[idx] for idx in range(X+1)]
dp[0] = dp[1] = [1]
if X >= 2:
    dp[2] = [1, 2]
if X >= 3:
    dp[3] = [1, 3]

for num in range(4, X+1):
    ans = len(dp[num-1]) + 1
    idx = num-1

    if num % 2 == 0 and len(dp[num//2])+1 <= ans:
        idx = num//2
        ans = min(ans, len(dp[num//2]) + 1)
    
    if num % 3 == 0 and len(dp[num//3])+1 <= ans:
        idx = num//3
        ans = min(ans, len(dp[num//3]) + 1)
    
    dp[num] = dp[idx].copy()
    dp[num].append(num)


print(len(dp[X])-1)
dp[X].sort(reverse=True)
for num in dp[X]:
    print(num, end=' ')
