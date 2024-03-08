import sys
input = sys.stdin.readline

def get_day(withdraw_money, days):
    tot_withdraw_count = 0 # 인출 횟수
    current_money = 0

    for money in days:
        if money > current_money:
            tot_withdraw_count += 1            
            current_money = withdraw_money
        
        current_money -= money

    return tot_withdraw_count

def binary_search(days):
    left = max(days) # 500
    right = sum(days) # 1901
    mid = (left + right) // 2 # 1200

    answer = 0
    while left <= right:
        mid = (left + right) // 2
        tot_withdraw_count = get_day(mid, days)

        if tot_withdraw_count == withdraw_count: answer = mid

        if tot_withdraw_count > withdraw_count: left = mid + 1
        else: right = mid - 1

    return answer or mid

day, withdraw_count = map(int, input().split())
days = [int(input()) for _ in range(day)]

answer = binary_search(days)
print(answer)