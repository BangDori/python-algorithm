import sys
input = sys.stdin.readline

MOD = int(1e9)+7
N, K = map(int, input().split())

top = 1; down = 1
for num in range(K):
    top *= (N-num)
    top %= MOD

for num in range(1, K+1):
    down *= num
    down %= MOD

down = pow(down, -1, MOD)
print((top * down) % MOD)