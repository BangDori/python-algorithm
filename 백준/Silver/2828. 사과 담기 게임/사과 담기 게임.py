import sys
input = sys.stdin.readline

screen_width, basket_width = map(int, input().split())
apples = int(input())

basket_start = 1
basket_end = basket_width

total_move_distance = 0
for _ in range(apples):
    apple_drop = int(input())

    move_distance = 0
    if apple_drop < basket_start:
        move_distance = basket_start - apple_drop
        basket_start -= move_distance
        basket_end -= move_distance
    elif apple_drop > basket_end:
        move_distance = apple_drop - basket_end
        basket_start += move_distance
        basket_end += move_distance

    total_move_distance += move_distance

print(total_move_distance)