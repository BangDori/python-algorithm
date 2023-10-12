"""
    2 sec, 512 MB

    제일 왼쪽 -> 제일 오른쪽 이동

    1km 마다 1리터의 기름
"""

import sys
input = sys.stdin.readline

country = int(input())
road_length = list(map(int, input().split()))
liter_prices = list(map(int, input().split()))
liter_prices.pop()

answer = 0
liter = 0

min_liter_price = liter_prices[0]
min_idx = 0

for idx in range(len(road_length)):
    if liter < road_length[idx]:
        if min_liter_price > liter_prices[idx]:
            min_liter_price = liter_prices[idx]
            min_idx = idx

        liter = road_length[idx]
        answer += (liter * min_liter_price)
    
    liter -= road_length[idx]

print(answer)