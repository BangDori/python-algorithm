from collections import deque
import sys
input = sys.stdin.readline

coin_cnt, total_price = map(int, input().split())
coins = [int(input()) for _ in range(coin_cnt)]
new_coins = []

for coin in coins:
    if coin <= total_price: new_coins.append(coin)

count = [1e9 for _ in range(total_price+1)]
queue = deque([(0, 0)])
count[0] = 0

while queue:
    curr, cnt = queue.popleft()

    if count[curr] < cnt:
        continue

    for coin in new_coins:
        if curr+coin <= total_price and count[curr+coin] > cnt+1:
            count[curr+coin] = cnt+1
            queue.append((curr+coin, cnt+1))

print(count[total_price] if count[total_price] != 1e9 else -1)

# 2 5
# 2
# 3