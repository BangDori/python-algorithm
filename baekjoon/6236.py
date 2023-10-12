import sys
input = sys.stdin.readline

def getDay(withdraw_money, money_in_day):
    tot_withdraw = 0
    withdraw_count = 0 # 인출 횟수

    current_money = 0
    for money in money_in_day:
        if money > current_money:
            current_money = 0
            tot_withdraw += 1
            withdraw_count = money // withdraw_money if money % withdraw_money == 0 else (money // withdraw_money) + 1
            current_money = (withdraw_count * withdraw_money)
        
        current_money -= money

    return tot_withdraw


use_day, get_count = map(int, input().split())
money_in_day = [int(input()) for _ in range(use_day)]

left = max(money_in_day)
right = sum(money_in_day)
mid = (left + right) // 2

answer = 0
while left <= right:
    mid = (left + right) // 2

    withdraw_count = getDay(mid, money_in_day)

    if withdraw_count == get_count: answer = mid

    if withdraw_count > get_count:
        left = mid + 1
    else:
        right = mid - 1

if answer != 0:
    print(answer)
else:
    print(mid)