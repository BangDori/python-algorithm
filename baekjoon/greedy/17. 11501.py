import sys
input = sys.stdin.readline

def action(days, stock_prices):
    max_prices = [0 for _ in range(days)]

    max_price = 0
    for idx in range(days-1, -1, -1):
        if max_price < stock_prices[idx]:
            max_price = stock_prices[idx]
        
        max_prices[idx] = max_price

    use_money = 0
    buy_count = 0
    sell_money = 0
    for idx in range(days):            
        # 구매
        if stock_prices[idx] < max_prices[idx]:
            use_money += stock_prices[idx]
            buy_count += 1
            continue

        # 판매
        if stock_prices[idx] == max_prices[idx] and buy_count > 0:
            sell_money += buy_count * stock_prices[idx]
            buy_count = 0
            continue
    
    return sell_money - use_money

test_case = int(input())

for _ in range(test_case):
    days = int(input())
    stock_prices = list(map(int, input().split()))

    profit = action(days, stock_prices)
    print(profit)