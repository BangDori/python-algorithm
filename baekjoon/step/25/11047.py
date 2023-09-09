"""
    1 sec, 256 MB
"""

N, K = map(int, input().split())
prices = [int(input()) for _ in range(N)]
prices.sort(reverse=True)

answer = 0
while K > 0:
    count = K // prices[0]

    if count != 0:
        answer += count
        K -= count * prices[0]
    prices.pop(0)
print(answer)