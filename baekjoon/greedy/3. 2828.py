"""
    1 sec, 128 MB
    
    바구니 옮기기 게임

    스크린 N칸, 스크린 아래 M칸을 차지하는 바구니
    (M < N)
"""

import sys
input = sys.stdin.readline

screen, basket = map(int, input().split())
apple_count = int(input())
apple_coords = []

for _ in range(apple_count):
    apple_coords.append(int(input()))

current_coord = (1, 1*basket)
tot_move = 0

for apple in apple_coords:
    if apple >= current_coord[0] and apple <= current_coord[1]:
        continue

    if apple < current_coord[0]:
        tot_move += current_coord[0] - apple
        current_coord = (current_coord[0] - (current_coord[0]-apple), current_coord[1] - (current_coord[0]-apple))
    elif apple > current_coord[1]:
        tot_move += apple - current_coord[1]
        current_coord = (current_coord[0] + apple - current_coord[1], current_coord[1] + apple - current_coord[1])

print(tot_move)