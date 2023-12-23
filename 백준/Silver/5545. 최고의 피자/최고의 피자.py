# 1원당 열량이 가장 높은 피자
# 도우 가격 A원 토핑 가격 B원

import sys
input = sys.stdin.readline

topping_count = int(input())
dow_price, topping_price = map(int, input().split())
dow_calorie = int(input())

topping_calories = []
for _ in range(topping_count):
    tp_cl = int(input())
    topping_calories.append(tp_cl)
topping_calories.sort(reverse=True)

def get_total_calorie(current_calorie, topping_calorie):
    return current_calorie + topping_calorie

def get_pizza_price(topping_count):
    return dow_price + topping_price * topping_count

current_calorie = dow_calorie
current_topping_count = 0

for topping_calorie in topping_calories:
    next_calorie = get_total_calorie(current_calorie, topping_calorie)

    if current_calorie // get_pizza_price(current_topping_count) > next_calorie // get_pizza_price(current_topping_count+1):
        break

    current_calorie = next_calorie
    current_topping_count += 1

print(current_calorie // get_pizza_price(current_topping_count))